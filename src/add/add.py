
def add1(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    res = []
    for vector1, vector2 in zip(matrix1, matrix2):
        res.append([num1 + num2 for num1, num2 in zip(vector1, vector2)])
    return res


def add2(*matrices: list[list[list[int]]]) -> list[list[int]]:
    res = []
    try:
        for vectors in zip(*matrices, strict=True):
            res.append([sum(numbers) for numbers in zip(*vectors, strict=True)])
        return res
    except ValueError:
        raise ValueError("Given matrices are not the same size.")


def main():
    # Base exercise:
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    res = add1(matrix1, matrix2)
    expected_res = [[3, -3], [-3, 3]]
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    res = add1(matrix1, matrix2)
    expected_res = [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 1
    matrix1 = [[1, 9], [7, 3]]
    matrix2 = [[5, -4], [3, 3]]
    matrix3 = [[2, 3], [-3, 1]]
    res = add2(matrix1, matrix2, matrix3)
    expected_res = [[8, 8], [7, 7]]
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 2
    try:
        res = add2([[1, 9], [7, 3]], [[1, 2], [3]])
    except ValueError:
        pass


if __name__ == "__main__":
    main()
