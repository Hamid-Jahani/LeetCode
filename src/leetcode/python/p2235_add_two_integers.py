"""2235. Add Two Integers (Easy)

https://leetcode.com/problems/add-two-integers/

Given two integers num1 and num2, return their sum.

Constraints: -100 <= num1, num2 <= 100.
"""

from __future__ import annotations


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        """Return num1 + num2.

        Shadows the builtin ``sum`` because LeetCode's signature for this
        problem names the method that way; the builtin is unaffected outside
        the class body.
        """
        return num1 + num2
