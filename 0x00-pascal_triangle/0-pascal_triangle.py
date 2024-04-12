#!/usr/bin/python3
"""
Returns a list of lists
representing Paascal's triangle
"""

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle
