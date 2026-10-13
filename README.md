# Channels

A Quill for [Cloudmorrow](https://github.com/Cloudmorrow/cloudmorrow): a
team's conversations, on your own server.

- **Public channels** are everybody's: everybody is in them, anybody writes
  in them, and nobody leaves.
- **Private channels** are the people added to them. Nobody accepts an
  invitation — you are added, you are told, and you can leave.
- **Direct messages** are between two people. Pick somebody and the
  conversation is there, whether or not it was a moment ago, from either side.
- **Threads.** Reply under a message and the replies stay with it: beside
  the conversation on a computer, a page on a phone, indented in the
  terminal. The channel stays readable.
- **@mentions.** Write `@name` and that person gets a push that says so —
  *bram mentioned you in #general* — if they are in the channel. The box
  offers names as you type an @.
- **Reactions.** One tap puts your 👍 on a message; yours again takes it
  back. Six to choose from, counted under the line.
- **Pinned messages.** A message's author, or whoever manages the channel,
  keeps it at the top; the channel's header counts them and opens the list.
- Everybody starts with `#general`.
- What you have not read is counted beside each channel and on the app's
  icon, and everybody else in a channel gets a push when somebody writes.
- A channel's topic and every message are sealed at rest; a message is its
  author's to change or delete.

## Channels replaces Chat

The same channels and messages, with threads, mentions, reactions and
pinned messages on top: Channels reads the channel and message datamodels
Chat kept, so every conversation is already here. Install Channels, switch
Chat off, and nothing is lost; the `#general` Chat made is the one Channels
uses.

## Using it

There are three kinds of channel, and the kind *is* the access rule — there
is nothing else to check, and no permissions screen:

- **Public.** Everybody is in it. It is in everyone's list, anyone may write
  in it, and nobody can leave — leaving a room everybody is in is a mute, and
  a mute is not this. `#general` is one, made once for the whole server the
  first time anybody opens Channels.
- **Private.** The people in it. Anyone can make one and put people in it;
  there is no invitation to accept. You are added, you get a notification
  saying so, and you can leave. Its maker can take somebody out, and anybody
  in it can add somebody.
- **Direct.** Two people, and it is never made from a form. Pick `ada` and
  the conversation with her is there, whether or not it existed a moment
  ago; `ada` picking you finds the same one. It is called after the other
  person.

Everyone can write to everyone; there is no setting for that. A channel is
its maker's to rename, re-topic or delete (and an administrator's); a
message is its author's to change or take back.

**Unread** is when you last looked: everything somebody else wrote in a
channel after that is unread, and opening the channel — on any device —
moves it on. Writing in a channel reads it. Somebody added to a channel
counts from when they were added, and a new account counts the public
channels from when it was made: the history is there to scroll back
through, but a year of it is not a badge.

**Talking:**

#### In the web app

The **Channels** tab: the channels, with what is unread in each, then a
conversation, newest at the bottom; on a computer both side by side. The
pen beside the title makes a channel — everybody's, or the people you
pick — and the people icon starts a direct message. Write `@name` and the box
offers names; tap a message for its thread, its reactions, or to pin it.
Push wakes the app the moment somebody writes.

#### In the terminal app

The **Channels** card (`f4`): channels on the left, the conversation on the
right. `n` makes a channel, `m` writes to one person, `a` adds somebody,
`e` renames or deletes one of yours, `l` leaves it; on a line, `r` replies
in its thread, `x` reacts, `p` pins it.

#### On the command line

```
cm channels list                          # the channels, with what is unread in each
cm channels show general                  # the conversation, newest at the bottom
cm channels say general "on my way"       # a channel by name, or the person
cm channels reply general 3f2a "me too"   # a line is named by the start of its id, in the margin
cm channels show general --thread 3f2a
cm channels react general 3f2a 👍         # yours again takes it back
cm channels pin general 3f2a              # or unpin
```

---

An assistant reaches it with the generic record tools. Neither client holds
a socket open: a conversation on screen asks for what changed since its
newest line every few seconds, and a push wakes it the moment something
arrives, so the server stays a plain request-and-response thing that a
phone on a train reconnects to without noticing. An administrator can
switch it off like any other Quill: the tab goes and the API answers 403.
Removing the Quill takes its tab and nothing else; the channels and
messages are records, and stay.

## What it adds to your Cloudmorrow

| | |
| --- | --- |
| Datamodels | uses the foundational `channel` (a space: shared or public), `message` (in a channel, authored, with `reply_to` and `pinned`, notifies with push and unread) and `reaction` (one person's emoji on a message) — domain *Messaging* |
| Screens | one `thread`, with `reply_to`, `pinned`, `reactions` and `mentions`: the channels, and the conversation — on the phone, the web app, the terminal, `cm channels`, and to your assistant |
| Jobs | none |
| Datasets | `general`: one public channel for the whole server, the first time anybody opens Channels (unless Chat made it already) |
| Services, webhooks, APIs | none |

It contains no code: everything above is declared in [`quill.toml`](quill.toml).

## Working on it

See [CLAUDE.md](CLAUDE.md) and the skills in `.claude/skills/`. In short:

```
uv sync                  # .venv with Cloudmorrow and pytest
cm quill check           # the manifest, as a server would install it
cm quill test            # tests/, against the real record store and gate
cm quill test --sandbox  # the same, with the code in the sandbox
cm quill dev --local     # a throwaway server here, reinstalled as you save
```

## Licence

AGPL-3.0-or-later.
