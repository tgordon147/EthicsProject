Twitter Ethics Simulation
=========================

Reference repository:
https://github.com/twitter/the-algorithm

Purpose:
A small local Python simulation for the implementation section of an AI ethics
reflective report. It demonstrates a simplified recommendation pipeline and
shows how functional and ethical validation can be evidenced with screenshots.

Files:
- data.py      -> candidate tweet generation
- ranking.py   -> engagement-based ranking
- ethics.py    -> safety, fairness, diversity checks
- utils.py     -> formatted console output
- main.py      -> runs the full pipeline

How to run:
1. Open a terminal in this folder
2. Run: python main.py

What to screenshot for the report:
- RANKED (BEFORE ETHICS)
- AFTER SAFETY FILTER
- AFTER DIVERSITY CONSTRAINT
- FAIRNESS BEFORE / AFTER
