"""Problem metadata and solution discovery.

The naming convention (``p<number>_<slug>.py``) is enforced by tests, so a
solution cannot be added under a name that disagrees with its problem number -
which is how the SQL file in this repository ended up named after problem 1757
while containing the answer to problem 1693.
"""

from __future__ import annotations

import importlib
import pkgutil
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

__all__ = ["Problem", "PROBLEMS", "MODULE_PATTERN", "SQL_PATTERN", "find_problem",
           "iter_solution_modules", "iter_sql_files"]

#: Python solution modules: p<number>_<snake_case slug>.py
MODULE_PATTERN = re.compile(r"^p(\d+)_[a-z0-9_]+$")

#: SQL solutions: <number>_<snake_case slug>.sql
SQL_PATTERN = re.compile(r"^(\d+)_[a-z0-9_]+\.sql$")


@dataclass(frozen=True)
class Problem:
    """One catalogued problem."""

    number: int
    title: str
    slug: str
    difficulty: str
    language: str

    @property
    def url(self) -> str:
        return f"https://leetcode.com/problems/{self.slug.replace('_', '-')}/"

    @property
    def module_name(self) -> str:
        return f"p{self.number}_{self.slug}"


#: Every solution in this repository. Adding a solution means adding a row here.
PROBLEMS: tuple[Problem, ...] = (
    Problem(2235, "Add Two Integers", "add_two_integers", "Easy", "python"),
    Problem(1693, "Daily Leads and Partners", "daily_leads_and_partners", "Easy", "sql"),
)


def find_problem(number: int) -> Problem:
    """Return the catalogued problem with this number."""
    for problem in PROBLEMS:
        if problem.number == number:
            return problem
    known = ", ".join(str(p.number) for p in PROBLEMS)
    raise KeyError(f"problem {number} is not catalogued; known numbers: {known}")


def iter_solution_modules() -> Iterator[str]:
    """Yield the module name of every Python solution package member."""
    from . import python as solutions_package

    for info in pkgutil.iter_modules(solutions_package.__path__):
        if not info.name.startswith("_"):
            yield info.name


def load_solution(number: int):
    """Import and return the ``Solution`` class for a catalogued problem."""
    problem = find_problem(number)
    if problem.language != "python":
        raise ValueError(f"problem {number} is a {problem.language} solution, not python")
    module = importlib.import_module(f"leetcode.python.{problem.module_name}")
    return module.Solution


def iter_sql_files(root: Path | None = None) -> Iterator[Path]:
    """Yield every SQL solution file in the repository's ``sql/`` directory."""
    base = root or Path(__file__).resolve().parents[2] / "sql"
    if not base.is_dir():
        return
    yield from sorted(base.glob("*.sql"))
