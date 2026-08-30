# LeetCode

A collaborative, group-maintained collection of [LeetCode](https://leetcode.com/) solutions in Python and SQL — catalogued, tested, and checked for consistency.

**Tech stack:** Python 3 · MySQL · pytest

---

## Overview

Solutions are organised by problem number rather than by free-form title, and every one is registered in a central catalogue. Tests run each solution against the examples from its own problem statement, and separate structural tests verify that filenames, catalogue entries, and file headers all agree.

That last part exists for a reason: this repository previously contained a SQL file named *Recyclable and Low Fat Products* (problem 1757) whose contents were the answer to *Daily Leads and Partners* (problem 1693). Nothing caught it. Now something does.

## What's inside

```
LeetCode/
├── src/leetcode/
│   ├── registry.py                       # Problem catalogue and discovery
│   └── python/
│       └── p2235_add_two_integers.py     # One module per problem
├── sql/
│   └── 1693_daily_leads_and_partners.sql
├── tests/
│   ├── test_solutions.py                 # Correctness, from LeetCode's examples
│   └── test_conventions.py               # Naming and catalogue consistency
└── pyproject.toml
```

## Conventions

| Kind | Location | Filename |
|---|---|---|
| Python | `src/leetcode/python/` | `p<number>_<snake_case_slug>.py` |
| SQL | `sql/` | `<number>_<snake_case_slug>.sql` |

Every solution also needs a row in `PROBLEMS` in `registry.py`:

```python
Problem(2235, "Add Two Integers", "add_two_integers", "Easy", "python")
```

Python solutions keep LeetCode's `Solution` class shape, so a file can still be pasted straight into the online editor.

## Adding a solution

1. Create the file using the naming convention above.
2. Add a `Problem(...)` row to `PROBLEMS`.
3. Add test cases in `tests/test_solutions.py`, taken from the problem's own examples plus its stated constraint boundaries.
4. Run `pytest`.

The structural tests will fail if the filename, the catalogue entry, and the SQL header comment disagree about which problem the file solves.

## Usage

```bash
pip install -e ".[dev]"
pytest
```

```python
from leetcode.registry import load_solution, find_problem

solve = load_solution(2235)().sum
print(solve(12, 5))            # 17

print(find_problem(1693).url)  # https://leetcode.com/problems/daily-leads-and-partners/
```

## Corrections applied during the restructure

- **The SQL solution was filed under the wrong problem.** `Recyclable and Low Fat Products.sql` (1757) contained a `GROUP BY date_id, make_name` query over `DailySales` — the answer to 1693, *Daily Leads and Partners*. Renamed to match its actual content, and `test_sql_header_number_matches_the_filename` now guards against a repeat.
- **PyCharm template boilerplate was committed.** The Python solution opened with `# This is a sample Python script.` / `# Press Shift+F10 to execute it...`, left over from the IDE's new-file template.
- **JetBrains `.idea/` configuration was tracked** (8 files) and has been untracked, with a `.gitignore` added.
- **No tests existed.** Solutions were unverified; a wrong answer would sit in the repository indefinitely.

## Solutions

| # | Problem | Difficulty | Language |
|---|---|---|---|
| 1693 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/) | Easy | SQL |
| 2235 | [Add Two Integers](https://leetcode.com/problems/add-two-integers/) | Easy | Python |

## License

Released under the [GNU GPL v3.0](LICENSE).
