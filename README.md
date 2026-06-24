# LeetCode

A collaborative, group-maintained collection of [LeetCode](https://leetcode.com/) solutions, organized by language. The aim is to solve problems together and keep clean, readable reference implementations in Python and SQL (with room to grow into other languages over time).

**Tech stack:** Python 3 · MySQL

## Overview

This repository groups LeetCode solutions by the language used to solve them. Each top-level folder holds standalone solution files, one per problem, named after the problem. The collection is intentionally simple and incremental — solutions are added as the group works through problems.

## What's inside

```
LeetCode/
├── Python/                       # Python solutions
│   └── Add Two Integers.py       # Solution class with a sum(num1, num2) method
├── SQL/                          # SQL solutions (MySQL dialect)
│   └── Recyclable and Low Fat Products.sql
├── LICENSE                       # GNU GPL v3.0
└── README.md
```

- **Python/** — Solutions follow LeetCode's conventional `Solution` class pattern, with the answer implemented as a typed method.
- **SQL/** — MySQL query statements written directly against the problem's table schema.

## Approach

- **Python:** Each problem is implemented as a method on a `Solution` class with type hints, matching the structure LeetCode expects when you submit. For example, *Add Two Integers* exposes `Solution.sum(self, num1: int, num2: int) -> int`.
- **SQL:** Queries are written in standard MySQL syntax, using aggregation (`GROUP BY`, `COUNT(DISTINCT ...)`) where the problem calls for it.

## How to run

Solutions are designed to be pasted into the LeetCode editor for the corresponding problem. To run a Python solution locally, instantiate the `Solution` class and call its method:

```python
# Example: Add Two Integers
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

print(Solution().sum(12, 5))  # -> 17
```

For the SQL solutions, run the query in a MySQL client against the table described in the corresponding LeetCode problem.

## Contributing

This is a group project. To add a solution:

1. Place the file in the folder for its language (`Python/`, `SQL/`, etc.).
2. Name the file after the LeetCode problem.
3. Keep the implementation clean and follow the language's conventional solution structure.

## License

Released under the [GNU General Public License v3.0](LICENSE).
