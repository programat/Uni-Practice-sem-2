# Дана квадратная матрица A размерности n x n. Привести ее к нижне-треугольной форме.
# Чтение производится из файла
from random import randint

def init_matrix():
    a = []
    print('Ввод элементов через пробел, для завершения нажмите enter')
    a.append(list(map(float, input().split())))
    col = len(a[0])
    while (True):
        tmp = list(map(float, input().split()))
        if len(tmp) == col:
            a.append(tmp)
        # else:
        #     print('Эта строка считана не будет', end=" ")
        if tmp == []:
            break
    return a

def rand_matrix(test_num):
    a = []
    counter = 0
    for i in range(test_num):
        a = []
        n = randint(3, 10)
        for i in range(n):
            a.append([0]*n)
            for j in range(n):
                a[i][j] = randint(-1000, 1000)
        test_Laplas = Laplas(a)
        test_det = float(det(a))
        if test_Laplas != test_det:
            print(f'Лаплас = {test_Laplas}, Дет = {test_det}, разница = {abs(test_Laplas - test_det)}')
            print()
            counter+=1
    print(counter)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])

def swap_row(matrix, i):
    if(matrix[i][i] == 0):
        for j in range(len(matrix)):
            if matrix[j][i] != 0:
                matrix[j], matrix[i] = matrix[i], matrix[j]
                break
        return matrix
    else: return matrix

def Triangle_2(array): return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])

def Triangle(array):
    # eсли определитель имеет второй порядок:
    if len(array) == 2:
        return Triangle_2(array)

    # дозаполнение массива для решения методом "ленивого треугольник"
    for i in range(3):
        for j in range(2):
            array[i].append(array[i][j])

    # часть с плюсом: [i,i], [i,i+1], [i,i+2]
    plus, minus = 0, 0
    temp = 1
    n = len(array)
    for i in range(n):
        for j in range(n):
            temp *= array[j][j + i]
        plus += temp
        temp = 1
        for l in range(n):
            temp *= array[n - 1 - l][l + i]
        minus += temp
        temp = 1
    return plus - minus

def Laplas(array):
    n = len(array)
    temp = [[]] * (n - 1)
    ans = [0] * n
    for i in range(n):  # 0, 1, 2, 3 - коэффициенты
        for j in range(n - 1):  # 0, 1, 2 - строки минора
            temp[j] = array[j + 1][:i] + array[j + 1][i + 1:]
        if len(temp) == 3:
            ans[i] = array[0][i] * ((-1) ** i) * Triangle(temp)
        elif len(temp) > 3:
            ans[i] = array[0][i] * ((-1) ** i) * Laplas(temp)
        else:
            return 0
        temp = [[]] * (n - 1)
    return sum(ans)

def det(matrix):
    for i in range(len(matrix)-1): #цикл, который отвечает за переход к строке, которую будем домножать
        if(matrix[i][i] == 0.0): matrix = swap_row(matrix, i)
        for j in range(i+1, len(matrix)): #цикл, который отвечает за строку от которой будем отнимать
            difference = round((matrix[j][i] / matrix[i][i]), 6) * (-1)
            for l in range(len(matrix)): #цикл, который отвечает за обход элементов на одной строке
                matrix[j][l] += difference*matrix[i][l]
    determinant = 1
    for i in range(len(matrix)):
        determinant *= matrix[i][i]
    # return ('%f' % determinant).rstrip('0').rstrip('.')
    return round(determinant, 6)

rand_matrix(20)
# print(det(init_matrix()))

