# import numpy as np
# import matplotlib as plt

# palette = np.array([[0, 0, 0],[255, 0, 0], [0, 255, 0], [0,0,255],[255,255,255]], dtype = uint8)

# image = np.array
# у меня лапки, поэтому пишу проход улиткой
def ulitka(N, M):


    m = [[0]*M for _ in range(N)]

    number = 1
    top = 0
    bottom = N-1
    left = 0
    right = M-1


    while left <= right and top <= bottom:
# условие нахождения внутри матрицы на каждом этапе
    

        for i in range(left, right + 1):
            m[top][i] = number
            number +=1
        top += 1
# проход по первой строчке            

        
        for j in range(top, bottom + 1):
            m[j][right] = number
            number += 1
        right -= 1
# проход по правому столбцу
# на повороте улитка просто второй раз переобозначает ячейку тем же числом, можно это исправить, но зачем не ясно       
        if top <= bottom:
            for i in range(right, left -1, -1):
                m[bottom][i] = number
                number += 1 
            bottom -= 1
# проход по нижней строке
# теперь нужно добавить что-то к top, чтобы улитка не вышла на уже заполненую строку наверно +1
        if left <= right:
            for j in range(bottom, top - 1 , -1):
                m[j][left] = number
                number += 1
            left += 1
# проход по левой строке вверх, теперь можно отрезать крайнюю левую и крайнюю правую, а также низ
#  (хотя можно было и раньше отрезать право с низом, хз повлияет ли)
# кстати, а если матрица - не квадрат???
        
        
        
# есть подозрение что на следующем шаге в левую верхню строку будет воткнуто то же число, что и в предыдущую, но при этом индекс left уже будет другим
# поэтому добавлю в number еще 1
# замечу, что при проходе    
    return m
N = int(input())
M = int(input())

matrix = ulitka(N,M)

# при тесте 3 на 4 в правый (индекс: 2) столбец вписывается лишний элемент
# надо добавить ограничение на операции в обратном порядке( с проходом снизу вверх и справа налево)
# победа
def result(matrix):
    res = []
    
    for index, line in enumerate(matrix, 1):
       new_line = [x * index for x in line]
       res.append(new_line) 
    return res
for lines in result(ulitka(N, M)):
    print(*lines)

