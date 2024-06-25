#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for a in range(1, n + 1):
            level = []
            m = 1
            for b in range(1, a + 1):
                level.append(m)
                m = m * (a - b) // b
            res.append(level)
    return res
