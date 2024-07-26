#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
	"""
	Generates Pascal's triangle of n rows.

	:param n: Number of rows in Pascal's triangle
	:return: List of lists of integers representing Pascal's triangle
	"""
	triangle = []
	if n > 0:
		triangle = [[1]]
		for i in range(1, n):
			row = [1]
			for j in range(1, i):
				row.append(triangle[i-1][j-1] + triangle[i-1][j])
			row.append(1)
			triangle.append(row)
	return triangle
