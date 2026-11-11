# AI for Scientific Coding · Part 2 challenges

Twenty short, self-contained exercises that show what AI coding assistants can and cannot do, built
for Earth-science researchers. They work with **any** AI tool: a chat window (ChatGPT, Claude, Gemini),
an IDE assistant (VS Code Copilot, Cursor, Zed), a terminal agent (Claude Code, Codex) or a local model.
Nothing here depends on a particular editor, notebook or model.

## How this works
- Pick any challenge. They are independent. Numbers suggest a rough order from warm-up to stretch, not a
  sequence you must follow. Two hours is enough for five to eight if you talk about them, more if you don't.
- Each folder has a `README.md` brief with the situation, the task, how to check the result, and a
  reflection question that points back to the morning's slides. Most have code or data to copy and paste.
- Checking is the point. Most challenges include a check script or an expected output. Do not take the
  AI's word that something works. Run the check.
- Work in pairs if you can. One drives, one reads the AI's output critically. Swap halfway.

## What you need
Very little. The supplied scripts and checkers import only `numpy` and `pandas`; `matplotlib` is handy for
the challenges where you ask the AI to draw something. Any Python 3.9 or later will do. Nothing else is
required: no netCDF, no xarray, no notebook, no particular editor.

**Already have Python with numpy and pandas?** You are done. Check with:
```
python -c "import numpy, pandas; print('ready')"
```
If that prints `ready`, skip the rest of this section. If a module is missing:
```
pip install numpy pandas matplotlib
```

**Prefer a fresh environment?** Either of these creates one called `ai_challenges`:
```
conda env create -f environment.yaml
conda activate ai_challenges
```
or, without conda:
```
python -m venv ai_challenges
source ai_challenges/bin/activate      # Windows: ai_challenges\Scripts\activate
pip install numpy pandas matplotlib
```

Clone or download this repository. Open a terminal in a challenge folder to run things.

## How to feed a challenge to your tool
- **Chat window:** open the file, select all, paste. Say what it is: "Here is a Python script and the
  error it produces." Context is cheap; give it.
- **IDE assistant:** open the folder as a workspace and reference the file in chat (most tools let you
  `@file` or drag it in).
- **Terminal agent:** `cd` into the challenge folder and paste the task from the README. It can read the
  files itself. Watch what it does.
- **Local model:** same as a chat window. Expect weaker results on the longer challenges; that is useful
  information in itself.

## Habits worth practising today
1. Say who you are and what the context is before you ask.
2. Ask for one thing at a time. One function, one bug, one file.
3. Read what comes back before you run it. Then run it. Then check it.
4. When it is wrong, paste the failure back rather than fixing it yourself. See how many rounds it takes.
5. Ask "why" after it works. The explanation is what you keep.
6. End a prompt with "if this doesn't exist or the premise is wrong, say so" when you are not sure.

## The challenges
See `INDEX.md` for a one-table overview with time, difficulty and what each one shows.

## Licence and provenance
All code, text and data here are synthetic and written for this workshop. The "paper", "documentation"
and model log are fictional. Use and adapt freely.
