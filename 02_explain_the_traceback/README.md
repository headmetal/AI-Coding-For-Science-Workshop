# 02 · Explain the traceback

**Time:** 10 min · **Difficulty:** warm-up · **Shows:** the most useful everyday habit most people never try

## The situation
A colleague's analysis pipeline fails with the 40-line traceback in `traceback.txt`. They have sent you
the traceback and the code (`pipeline.py`) and asked "any idea?".

## Your task
1. **Without reading the code**, paste only `traceback.txt` into your AI tool and ask:
   "What went wrong, where, and what should I check?" Note how specific the answer is.
2. Now paste `pipeline.py` as well and ask again. Note what changed.
3. Ask for the fix. Apply it and run `python pipeline.py`. The script should print a single line
   ending in `OK`.

## How to check
`python pipeline.py` prints `Regional mean computed for 4 regions: OK`.

## Try this
- Ask it to explain the traceback as if to a first-year student. Then as a one-line Slack message.
- Ask: "Which line in the traceback is in *my* code, and which lines are inside numpy?"
  Learning to read that split is half the skill.

## Reflect
How much of the AI's first answer was a genuine diagnosis, and how much was a plausible-sounding guess
dressed up with the right vocabulary? What in the second answer told you the difference?
