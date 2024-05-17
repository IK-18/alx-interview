#!/usr/bin/python3
"""
N queens module
"""
import sys


solutions = []
"""
List of possible solutions
"""
n = 0
"""
Size of the chessboard
"""
pos = None
"""
List of possible positions
"""


def get_input():
    """
    Validates argument

    Returns:
        int: size of chessboard
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos_0, pos_1):
    """
    Checks if two queens are in attack position

    Args:
        pos_0 (list or tuple): First queen's position
        pos_1 (list or tuple): Second queen's position

    Returns:
        bool: True if queens are in an attack position else False
    """
    if (pos_0[0] == pos_1[0]) or (pos_0[1] == pos_1[1]):
        return True
    return abs(pos_0[0] - pos_1[0]) == abs(pos_0[1] - pos_1[1])


def group_exists(group):
    """
    Checks if a group exists in the list of solutions

    Args:
        group (list of integers): List of possible positions

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for solution in solutions:
        i = 0
        for solution_pos in solution:
            for group_pos in group:
                if solution_pos[0] == group_pos[0] and solution_pos[1] == group_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Builds solution

    Args:
        row (int): Current row in the chessboard
        group (list of lists of integers): Group of valid positions
    """
    global solutions
    global n
    if row == n:
        temp = group.copy()
        if not group_exists(temp):
            solutions.append(temp)
    else:
        for column in range(n):
            a = (row * n) + column
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
    Gets the solutions
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
