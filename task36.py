# Написать прогу, которая выдает матрицу по заданным параметрам

def create_matrix(colums, rows):
    list_1 = []
    for i in range (1, rows+1):
        for j in range (1, colums+1):
            list_1.append(j*i)
        print(*list_1)
        list_1 = []
   

colums = int(input('Введите количество столбцов:'))
rows = int(input('Введите количество строк:'))

print(create_matrix(colums,rows))
      
