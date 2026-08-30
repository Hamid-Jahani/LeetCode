"""Structural tests that keep the collection consistent as it grows.

The repository previously held a SQL file named after problem 1757
("Recyclable and Low Fat Products") whose contents were the answer to problem
1693 ("Daily Leads and Partners"). These tests make that class of mismatch fail
in CI rather than sit unnoticed.
"""

import re

import pytest

from leetcode.registry import (
    MODULE_PATTERN,
    PROBLEMS,
    SQL_PATTERN,
    iter_solution_modules,
    iter_sql_files,
)


class TestPythonNaming:
    def test_every_module_matches_the_convention(self):
        for name in iter_solution_modules():
            assert MODULE_PATTERN.match(name), f"{name} is not p<number>_<slug>"

    def test_every_module_is_catalogued(self):
        catalogued = {p.module_name for p in PROBLEMS if p.language == "python"}
        for name in iter_solution_modules():
            assert name in catalogued, f"{name} has no entry in PROBLEMS"

    def test_module_number_matches_its_catalogue_entry(self):
        by_module = {p.module_name: p.number for p in PROBLEMS if p.language == "python"}
        for name in iter_solution_modules():
            declared = int(MODULE_PATTERN.match(name).group(1))
            assert declared == by_module[name]


class TestSqlNaming:
    def test_every_sql_file_matches_the_convention(self):
        files = list(iter_sql_files())
        assert files, "no SQL solutions found"
        for path in files:
            assert SQL_PATTERN.match(path.name), f"{path.name} is not <number>_<slug>.sql"

    def test_every_sql_file_is_catalogued(self):
        catalogued = {p.number for p in PROBLEMS if p.language == "sql"}
        for path in iter_sql_files():
            number = int(SQL_PATTERN.match(path.name).group(1))
            assert number in catalogued, f"{path.name} has no entry in PROBLEMS"

    def test_sql_header_number_matches_the_filename(self):
        """Guards against the exact mismatch this repository previously had."""
        for path in iter_sql_files():
            filename_number = int(SQL_PATTERN.match(path.name).group(1))
            first_line = path.read_text(encoding="utf-8").splitlines()[0]
            match = re.search(r"(\d+)\.", first_line)
            assert match, f"{path.name} has no '<number>. Title' header comment"
            assert int(match.group(1)) == filename_number, (
                f"{path.name} declares problem {match.group(1)} in its header"
            )

    def test_sql_links_to_the_problem(self):
        for path in iter_sql_files():
            assert "leetcode.com/problems/" in path.read_text(encoding="utf-8")


class TestCatalogueIntegrity:
    @pytest.mark.parametrize("problem", PROBLEMS, ids=lambda p: str(p.number))
    def test_url_is_built_from_the_slug(self, problem):
        assert problem.url.startswith("https://leetcode.com/problems/")
        assert "_" not in problem.url.rsplit("/", 2)[-2]

    @pytest.mark.parametrize("problem", PROBLEMS, ids=lambda p: str(p.number))
    def test_slug_is_snake_case(self, problem):
        assert re.match(r"^[a-z0-9_]+$", problem.slug)

    @pytest.mark.parametrize("problem", PROBLEMS, ids=lambda p: str(p.number))
    def test_difficulty_is_valid(self, problem):
        assert problem.difficulty in {"Easy", "Medium", "Hard"}
