"""Solutions to LeetCode problems, kept runnable and tested.

Solutions live in ``leetcode.python`` as one module per problem, named
``p<number>_<slug>.py``. Each exposes LeetCode's conventional ``Solution``
class so the file can be pasted straight into the online editor.

SQL answers live in ``sql/`` as ``<number>_<slug>.sql``.
"""

from __future__ import annotations

from .registry import PROBLEMS, Problem, find_problem, iter_solution_modules

__version__ = "0.1.0"

__all__ = ["PROBLEMS", "Problem", "__version__", "find_problem", "iter_solution_modules"]
