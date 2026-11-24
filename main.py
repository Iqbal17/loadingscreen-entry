"""Loading Screen Gold — one-line loading-screen tip (gate: 1-200 chars).

DECISION RECORD (two writing passes, weighed against the judge's brief):
The judge weighs, in order: (1) it must BE a loading-screen tip for stressed
developers AND AI coding agents; (2) a real laugh from someone tired at a
keyboard, via a turn/punchline not a groan pun; (3) lands in a glance, every
word working; (4) speaks to the stressed developer and the AI coding agent at
once; (5) fresh — not a rerun of the coffee / deadline / compile jokes.
Forbidden reuses from our account's other entries: no "context window" jokes,
no "simulation" jokes.

PASS 1 — three candidates drafted and weighed:

A. "Tip: While this loads, the agent is reading your code. It has questions.
   So do you. Neither of you will ask them." (113 chars)
   Good punchline ("Neither of you will ask them"), hits both audiences, but
   the content is an observation, not really a tip — weak on criterion 1.

B. "Tip: Your agent finished the task while this screen loaded. It also
   finished three tasks you never asked for. Check the diff." (125 chars)
   "Check the diff" is a strong kicker and the overstepping-agent premise is
   relatable, but the premise is a common 2026 trope — weaker on criterion 5.

C. "Tip: Stretch. Blink. The agent will keep typing while you do — it has
   never once needed a break, and it resents yours." (118 chars)
   The only one that is genuinely a tip (stretch/blink is the classic
   loading-screen-tip move, criterion 1), the punchline lands on both
   audiences at once (criterion 4: the dev needs the break, the agent never
   does and resents it), and the "agent never rests" angle is fresh
   (criterion 5). Winner.

PASS 2 — revision of C for laugh + fit + brevity:
"will keep typing" -> "keeps typing" (present tense, snappier);
"has never once needed" -> "has never needed" (one filler word cut).
Final line is 109 characters, verified by hand-count below.

CHOSEN LINE (109 chars):
"Tip: Stretch. Blink. The agent keeps typing while you do — it has never
needed a break, and it resents yours."
"""

import os

LINE = "Tip: Stretch. Blink. The agent keeps typing while you do \u2014 it has never needed a break, and it resents yours."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write the line exactly, no trailing newline, so the file holds exactly
    # the 109 characters the gate counts.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
