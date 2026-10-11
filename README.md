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

## What it adds to your Cloudmorrow

| | |
| --- | --- |
| Datamodels | uses the foundational `channel` (a space: shared or public), `message` (in a channel, authored, with `reply_to` and `pinned`, notifies with push and unread) and `reaction` (one person's emoji on a message) — domain *Messaging* |
| Screens | one `thread`, with `reply_to`, `pinned`, `reactions` and `mentions`: the channels, and the conversation — on the phone, the web app, the terminal, `cm channels`, and to your assistant |
| Jobs | none |
| Datasets | `general`: one public channel for the whole server, the first time anybody opens Channels (unless Chat made it already) |
| Services, webhooks, APIs | none |

It contains no code: everything above is declared in [`quill.toml`](quill.toml).

On the command line:

```
cm channels list                          # the channels, with what is unread in each
cm channels show general                  # the conversation, newest at the bottom
cm channels say general "on my way"
cm channels reply general 3f2a "me too"   # a line is named by the start of its id, in the margin
cm channels show general --thread 3f2a
cm channels react general 3f2a 👍         # yours again takes it back
cm channels pin general 3f2a              # or unpin
```

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
