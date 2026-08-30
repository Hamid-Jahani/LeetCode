"""Tests for the catalogued solutions.

Cases are taken from each problem's own examples on LeetCode, plus the
boundaries stated in its constraints.
"""

import pytest

from leetcode.registry import PROBLEMS, load_solution


class TestAddTwoIntegers:
    """2235. Add Two Integers."""

    @pytest.fixture
    def solve(self):
        return load_solution(2235)().sum

    @pytest.mark.parametrize(
        "num1,num2,expected",
        [
            (12, 5, 17),    # LeetCode example 1
            (-10, 4, -6),   # LeetCode example 2
        ],
    )
    def test_leetcode_examples(self, solve, num1, num2, expected):
        assert solve(num1, num2) == expected

    @pytest.mark.parametrize(
        "num1,num2,expected",
        [
            (0, 0, 0),
            (100, 100, 200),      # upper bound of the stated constraints
            (-100, -100, -200),   # lower bound
            (-100, 100, 0),
        ],
    )
    def test_constraint_boundaries(self, solve, num1, num2, expected):
        assert solve(num1, num2) == expected

    def test_is_commutative(self, solve):
        assert solve(7, -3) == solve(-3, 7)


class TestCatalogue:
    def test_every_problem_has_a_distinct_number(self):
        numbers = [p.number for p in PROBLEMS]
        assert len(numbers) == len(set(numbers))

    def test_every_python_problem_loads(self):
        for problem in PROBLEMS:
            if problem.language == "python":
                assert load_solution(problem.number) is not None

    def test_loading_a_sql_problem_as_python_is_rejected(self):
        with pytest.raises(ValueError, match="not python"):
            load_solution(1693)

    def test_unknown_problem_number_raises(self):
        with pytest.raises(KeyError, match="not catalogued"):
            load_solution(999999)
