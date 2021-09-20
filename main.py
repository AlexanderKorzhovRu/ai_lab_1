import numpy as np


def generate_matrix(loc: int = 10, scale: int = 10, size: range = (100, 10)):
    matrix = np.random.normal(loc=loc, scale=scale, size=size)
    return matrix


def normalize_matrix(matrix, axis):
    mean = np.mean(matrix, axis=axis)
    sko = np.std(matrix, axis=axis)

    normalized_matrix = ((matrix - mean) / sko)
    return normalized_matrix


def find_matrix_lines_where_sum_more_then_value(matrix, value: int):
    sum_matrix_lines = np.sum(matrix, axis=1)
    return np.nonzero(sum_matrix_lines > value)


def merge_matrix(matrix_a_rows_count: int, matrix_b_rows_count: int):
    a = np.eye(matrix_a_rows_count)
    b = np.eye(matrix_b_rows_count)
    ab = np.vstack((a, b))
    return ab


def main():
    matrix = generate_matrix()
    normalized_matrix = normalize_matrix(matrix, 0)

    matrix = np.array([
        [4, 5, 0],
        [1, 9, 3],
        [5, 1, 1],
        [3, 3, 3],
        [9, 9, 9],
        [4, 7, 1]])
    matrix_lines = find_matrix_lines_where_sum_more_then_value(matrix, 10)

    merged_matrix = merge_matrix(3, 3)
    print(merged_matrix)


if __name__ == '__main__':
    main()
