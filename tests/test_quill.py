"""Channels' tests: the real record store, its spaces and gate, on this machine.

Channels has no code: everything it does is declared in quill.toml and done
by the core's spaces and the thread kit's team bindings. These hold what the
manifest promises.
"""

import pytest

from cloudmorrow.quill.testing import Harness


@pytest.fixture()
def q():
    with Harness(".") as harness:
        yield harness


def general(q):
    return next(c for c in q.list("channel") if c["name"] == "general")


def test_general_is_there_for_everybody(q):
    room = general(q)
    assert room["kind"] == "public"
    assert [c["name"] for c in q.as_user("sam").list("channel")] == ["general"]


def test_what_is_said_in_general_everybody_reads(q):
    room = general(q)
    q.seed("message", channel=room.id, body="morning all")
    said = q.as_user("sam").list("message", channel=room.id)
    assert [m["body"] for m in said] == ["morning all"]


def test_a_reply_lands_in_its_parents_channel_and_goes_with_it(q):
    room = general(q)
    parent = q.seed("message", channel=room.id, body="lunch?")
    reply = q.as_user("sam").seed("message", channel=room.id, body="yes", reply_to=parent.id)
    assert reply["channel"] == room.id and reply["reply_to"] == parent.id
    assert [m["body"] for m in q.list("message", reply_to=parent.id)] == ["yes"]
    q.delete("message", parent.id)
    assert q.list("message", channel=room.id) == []


def test_a_reaction_is_one_persons_and_theirs_to_take_back(q):
    room = general(q)
    line = q.seed("message", channel=room.id, body="shipped")
    sam = q.as_user("sam")
    mine = sam.seed("reaction", channel=room.id, message=line.id, emoji="🎉")
    assert [(r.owner, r["emoji"]) for r in q.list("reaction", message=line.id)] == [("sam", "🎉")]
    with pytest.raises(Exception):
        q.delete("reaction", mine.id)  # not sam's to take back
    sam.delete("reaction", mine.id)
    assert q.list("reaction", message=line.id) == []


def test_a_line_is_pinned_by_its_author_and_stays_the_authors(q):
    room = general(q)
    sam = q.as_user("sam")
    line = sam.seed("message", channel=room.id, body="read me")
    pinned = sam.change("message", line.id, pinned=True)
    assert pinned["pinned"] is True
    assert [m.id for m in q.list("message", channel=room.id, pinned=True)] == [line.id]


def test_a_mention_counts_as_unread_for_the_person_named(q):
    room = general(q)
    sam = q.as_user("sam")  # here already: what is written after is news to them
    q.seed("message", channel=room.id, body="@sam can you look at the NAS?")
    # The unread count and the last line are what the record store puts on a space for its asker.
    spaces = sam.state.records.list(sam._principal(), "channel")
    theirs = next(c for c in spaces if c.fields["name"] == "general")
    assert theirs.unread == 1 and theirs.last["title"].startswith("@sam")
