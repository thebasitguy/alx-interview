def pascal_triangle(n):
    """
    Generates Pascal's triangle of n rows.
    
    :param n: Number of rows in Pascal's triangle
    :return: List of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Compute the value for the current position by summing the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
