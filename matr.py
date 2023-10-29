def matrica(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left = 0
    right = n - 1
    top = 0
    bottom = n - 1

    while left <= right and top <= bottom:
        # Заполнение верхней горизонтальной строки
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Заполнение правого вертикального столбца
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Заполнение нижней горизонтальной строки в обратном порядке
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Заполнение левого вертикального столбца в обратном порядке
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

def matrica_right(matrix):
    n = len(matrix)
    matrix_b = [[0] * (2 * n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_b[i][j] = matrix[i][j]
            matrix_b[i][j+n] = matrix[i][n-j-1]
    return matrix_b

def matrica_down(matrix):
    n = len(matrix)
    matrix_c = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(2 * n):
            matrix_c[i][j] = matrix[i][j]
            matrix_c[2 * n - i - 1][j] = matrix[i][j]
    return matrix_c

# Пример использования
n = int(input("Введите размер матрицы"))
matrix_a = matrica(n)
matrix_b = matrica_right(matrix_a)
matrix_c = matrica_down(matrix_b)

# Вывод результатов
print("Матрица A:")
for row in matrix_a:
    print(row)

print("\nМатрица B:")
for row in matrix_b:
    print(row)

print("\nМатрица C:")
for row in matrix_c:
    print(row)