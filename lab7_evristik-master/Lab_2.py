import numpy as np

# min_val, max_val = int(input("Введите минимальную границу весов: ")), int(input("Максимальную границу: "))
min_val, max_val = 10, 20
# matrix_dim = (int(input("Введите количество строк матрицы: ")), int(input("Количество столбцов: ")))
matrix_dim = 6, 3
list_index = []
# matrix = np.random.randint(min_val, max_val, matrix_dim)
matrix = [
    [4, 8, 6],
    [7, 9, 8],
    [6, 4, 2],
    [3, 6, 4],
    [6, 5, 4],
    [8, 7, 9]
]
matrix = np.array(matrix)
sums = [sum(row) for row in matrix]

dict_sums = dict(enumerate(sums))

dict_sorted = dict(sorted(dict_sums.items(), key=lambda x: x[1], reverse=True))
matrix_sorted = np.array([matrix[index] for index in dict_sorted.keys()])

print(f"До сортировки:\n {matrix}\nСуммы строк:\n {dict_sums}")
print(f"После сортировки:\n {matrix_sorted}\nСуммы строк:\n", dict_sorted, "\n")

new_matrix = np.zeros(matrix_dim)

for i, row in enumerate(matrix_sorted):
    if i == 0:
        loc_min = min(row)
        ind = np.where(row == loc_min)
        list_index.append(ind[0][0])
        # temp_arr = [ind[0][0], loc_min]
        # print(ind[0][0], f" {loc_min}", sep=":", end="  ")
        new_matrix[i][ind[0][0]] += loc_min
        if i + 1 != matrix_dim[0]:
            new_matrix[i + 1] += new_matrix[i]
    else:
        loc_min = None
        min_index = 0
        min_el = 0
        for ind, elem in enumerate(row):
            temp_sum = (new_matrix[i][ind] + elem)
            if loc_min is None:
                loc_min = temp_sum
                min_index = ind
                min_el = elem
            elif temp_sum < loc_min:
                loc_min = temp_sum
                min_index = ind
                min_el = elem
        new_matrix[i][min_index] += min_el
        # print(min_index+1)
        list_index.append(min_index)
        if i + 1 != matrix_dim[0]:
            new_matrix[i + 1] += new_matrix[i]

# print("\n", matrix)
print("\n", new_matrix)
print("Max = ", max(new_matrix[matrix_dim[0] - 1]))
print(list_index)

# import numpy as np
#
# # создаем матрицу 3x3
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # выбираем минимальные элементы из матрицы
# min_elements = np.min(matrix, axis=1)
#
# # находим максимальный элемент из массива минимальных элементов
# max_element = np.max(min_elements)
# print(matrix)
# print(max_element)
