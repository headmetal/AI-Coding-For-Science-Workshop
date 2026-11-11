# 20 · Review my code

**Time:** 15 min · **Difficulty:** core · **Shows:** AI as a code reviewer, and how to calibrate its reviews

## The situation
`submission.py` is a small module a student has asked you to review before it goes into the group's
shared repository. It runs. It has at least seven things a careful reviewer would flag, ranging from
"will corrupt results" to "style".

## Your task
1. Review it yourself first. Five minutes, write down what you find.
2. Paste it and ask for a code review. Ask for findings ranked by severity, each with the line, the
   problem, why it matters, and the fix.
3. Compare lists. What did it find that you missed? What did you find that it missed? What did it
   flag that is not actually a problem?
4. Ask it to write the fixed version and a short, kind review comment you could actually send.

## How to check
The planted issues, roughly by severity: a mutable default argument that accumulates state across
calls; a bare `except:` that swallows a real error and returns a wrong value; integer division
semantics that silently differ for a Python 2 habit; a timezone-naive datetime compared with an aware
one (crashes on some inputs); a "reproducible" test that uses an unseeded random generator; a loop that
recomputes an expensive thing every iteration; a variable that shadows a builtin. Score the review
out of 7. Also count false alarms.

## Reflect
Reviews are where AI is most useful and least trusted. Was its tone right? Would you send its
comment as written? What does that tell you about using it for the human half of the job?
