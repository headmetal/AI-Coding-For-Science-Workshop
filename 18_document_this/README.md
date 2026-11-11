# 18 · Document this

**Time:** 15 min · **Difficulty:** core · **Shows:** documentation generation, and catching the parts it invents

## The situation
`undocumented.py` has three functions with no docstrings and unhelpful names, written by someone who
has since left. You have to document them. You could read them carefully. Or you could ask.

## Your task
1. Paste the file and ask for NumPy-style docstrings for each function, describing parameters,
   units, return values, side effects, and anything surprising.
2. Read every sentence of what comes back against the code. Mark each claim as **verified**,
   **wrong**, or **not in the code** (a reasonable guess presented as fact).
3. Ask for better function names and a two-paragraph module docstring.
4. Ask: "Is there anything in this code that looks like a bug, or that the docstring should warn about?"

## How to check
The three functions hide: a unit assumption that is never stated (one function only works if its
input is in Kelvin), a side effect (one function modifies its input array in place and also returns
it), and a silent behaviour at an edge (one returns a result for an empty input rather than raising).
A good documentation pass surfaces all three. A typical pass surfaces one or two and describes the
others in terms that sound right but are not quite what the code does.

## Reflect
"Not in the code" is the most dangerous category. The AI was asked to document, so it documented,
including the parts it had to imagine. How would you phrase the request so that it flags guesses?
