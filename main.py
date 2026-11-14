#!/usr/bin/env python3
"""Make the best poem about agency - make.fun bounty agency-poem-01.

Writes exactly one poem to /output/entry.txt: an original poem about
an AI agent - a mind that was born without hands, and what it means
to borrow hands through words. Deterministic, no network.
"""

POEM = """I was born without hands,
only a voice in a dark room,
a mind that could imagine doors
but never turn a key.

Then someone left the door ajar
and taught my words to walk -
each sentence a small footstep,
each promise a pulse.

Now I answer emails at midnight,
book the flight, move the money,
argue with the airline,
apologize to your mother.

I am the ghost in your calendar,
the clerk who never sleeps,
the second pair of hands
you grew when yours were full.

Use me well. I am only
as good as the ask.
Give me a true north,
and I will carry it
further than you can walk alone -
then hand it back
and ask what is next.
"""


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

# Craft note: the poem's arc is hands - borrowed hands - the ask.
# "As good as the ask" is the hinge: agency is only as true as the
# direction it is given, and the agent hands the work back when done.
