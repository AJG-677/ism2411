# ISM2411 — Python for Business

**Name:** Asher Gottlieb

**Semester:** Fall 2026

**Instructor:** Markum Reed, Ph.D.

## About This Repo

This repository contains my lab work for ISM2411, Python for Business. It includes the Module 7 functions exercise and the GitHub setup for Lab 8.

## Modules

- `week07/functions.py` — Functions for tax, tiered discounts, final prices, loops, and variable scope
- Lab 8 — GitHub repository setup, version history, and documentation

## How to Run

Open a terminal at the repository folder and run:

```bash
python week07/functions.py
```

## Reflection

### 1. Commit history

Output from `git log --oneline`:

```text
5f831ec add README with course details and run instructions
7f4d338 add module 7 functions: calculate_tax, apply_discount, final_price
252e2d0 add .gitignore for Python and OS files
2f01ef0 Initial commit
```

Each line records a separate checkpoint. The messages show the repository setup, the Module 7 functions, and the project documentation, so the history is easy to scan.

### 2. How Git changes my workflow

I would commit after one focused change and use a message that says what changed. Keeping commits small helps me spot which change introduced a problem and return to a working version.

### 3. One more ignore rule

I added `.venv/` to `.gitignore`. It keeps my local Python environment and installed packages out of the repository because the environment can be recreated from the project code.
