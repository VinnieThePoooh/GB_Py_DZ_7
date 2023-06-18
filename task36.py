# Написать прогу, которая выдает матрицу по заданным параметрам

colums = int(input('Введите количество столбцов:'))
rows = int(input('Введите количество строк:'))


def create_little_list(colums, rows):
    list_2 = []
    for i in colums:
        list_1 = [j*i for j in range (i, rows)]
        list_2.append(list_1)
    return list_2
print(create_little_list(colums,rows))

      
# list_2 = list(map(create_little_list(colums, rows),list_2))
# print (list_2)