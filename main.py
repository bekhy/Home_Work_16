# # 1
# a = 0
# mass = [10, 15, 22, 43, 58]
# for element in mass:
#     print(sum(mass))
#
# while element > a:
#     print(sum(mass))
#     a += 1

# # 1(def)
# a = 0
# mass = [10, 15, 22, 43, 58]
# def sum(x):
#     if x == []:
#         return 0
#     else:
#         return x[0] + sum(x[1:])
#
# print(sum(mass))


# # 2
# a = 0
# b = 0
# list_a = [1, 2, 3]
# list_b = [11, 22, 33]
# list_c = []
# for i in list_a:
#     for j in list_b:
#         if i not in list_c:
#             if j not in list_c:
#                 list_c.append(i)
#                 list_c.append(j)
# b += 1
# a += 1
# print(list_c)

# # 2(def)
# list_a = [1, 2, 3]
# list_b = [11, 22, 33]
# list_c = []
# def plus(x,y):
#     for i in range(len(x)):
#         list_c.append(x[i])
#         list_c.append(y[i])
#     return list_c
# print(plus(list_a, list_b))

# # 3
# print('Введите стороны треугольника:')
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a+b>c and b+c>a and c+a > b and a!=0 and b!= 0 and c!=0:
#     print('Такой треугольник есть')
# else:
#     print('Треугольник не существует')

# # 3(def)
# print('Введите стороны треугольника:')
# q = float(input("a = "))
# w = float(input("b = "))
# e = float(input("c = "))
# def treygolnik(a, b, c):
#     if a + b > c and b + c > a and \
#             c + a > b and a != 0 and \
#             b != 0 and c != 0:
#         return 'Такой треугольник есть'
#     else:
#         return 'Треугольник не существует'
# print(treygolnik(q, w, e))

# # 4
# import math
# long_1 = int(input("Введите долготу 1 точки: "))
# width_1 = int(input("Введите широту 1 точки: "))
# long_2 = int(input("Введите долготу 2 точки: "))
# width_2 = int(input("Введите широту 2 точки: "))
# R = 6371
# d = math.acos(math.cos((math.sin(width_1) *
# math.sin(width_2)) + (math.cos(width_1) *
# math.cos(width_2)) * math.cos(width_1 - width_2)))
# L = d * R
# print(L)

# 5


# # 6
# m = int(input("Введите количество строк: "))
# a = []
# for i in range(m):
#     a.append(input().replace("?", "*"))
# print(a)

# # 6(def)
# m = int(input("Введите количество строк: "))
# n = []
# def change(a):
#     for i in range(a):
#         n.append(input().replace("?", "*"))
#     return a
# print(change(m))

# # 7
# a = input("Введите дату используя \"-\": ")
# b = a.split("-")
# print(a + " -> " + b[2] + "/" + b[1] + "/" + b[0])

# # 7(def)
# a = input("Введите дату используя \"-\": ")
# b = a.split("-")
# def split_a(c):
#     return (a + " -> " + b[2] + "/" + b[1] + "/" + b[0])
# print(split_a(b))

# # 8
# a = 0
# c = 0
# b = float(input('Введите вес в граммах: '))
# a = b/1000
# print("В кг: ", str(a))
# c = a/1000
# print("В тонне: ", str(c))

# # 8
# b = float(input('Введите вес в граммах: '))
# def kg(a):
#     c = a / 1000
#     d = c / 1000
#     print("В кг: ", str(c))
#     print("В тонне: ", str(d))
# kg(b)

# # 9
# a= float(input("Длина коробки: "))
# b= float(input("Ширина коробки: "))
# c= float(input("Высота коробки: "))
# m= float(input("Длина двери: "))
# k= float(input("Ширина двери: "))
# if (a < m and a < k and b < k and b < m
#         or a < m and a < k and c < m and c < k
#         or c < m and c < k and b < m and b < k):
#     print("Коробка пролезет")
# else:
#     print("Не пролезет")

# # 9
# a = float(input("Длина коробки: "))
# b = float(input("Ширина коробки: "))
# c = float(input("Высота коробки: "))
# m = float(input("Длина двери: "))
# k = float(input("Ширина двери: "))
# def korobka(*args):
#     if (a < m and a < k and b < k and b < m
#             or a < m and a < k and c < m and c < k
#             or c < m and c < k and b < m and b < k):
#         print("Коробка пролезет")
#     else:
#         print("Не пролезет")
# korobka(a, b, c, m, k)

# # 10
# import math
# diametr = float(input("Введите диаметр поперечного сечения бревна: "))
# brus = float(input("Введите ширину бруса: "))
# s_brevno = (diametr / 2) ** 2 * math.pi
# s_brus = brus ** 2
# if s_brus < s_brevno:
#     print("Можно выпилить")
# else:
#     print("Нельзя")

# 10
import math
diametr = float(input("Введите диаметр поперечного сечения бревна: "))
brus = float(input("Введите ширину бруса: "))
s_brevno = (diametr / 2) ** 2 * math.pi
s_brus = brus ** 2
if s_brus < s_brevno:
    print("Можно выпилить")
else:
    print("Нельзя")

# # 11
# seat_number = int(input("Введите номер места: "))
# if seat_number > 36:
#     print("У вас боковое место!")
# elif seat_number < 1 and seat_number > 54:
#     print("Такого места нет!")
# elif seat_number % 2 == 1:
#     print("У вас нижнее место!")
# else:
#     print("У вас верхнее место!")

# # 12
# sum_count = float(input("Введите сумму: "))
# count500 = sum_count // 500
# sum500 = sum_count % 500
# count100 = sum500 // 100
# sum100 = sum500 % 100
# count10 = sum100 // 10
# sum10 = sum100 % 10
# count2 = sum10 // 2
# sum2 = sum10 % 2
# print("Кол-во купюр по 500: " + str(count500) +
#       "\nКол-во купюр по 100: " + str(count100) +
#       "\nКол-во купюр по 10: " + str(count10) +
#       "\nКол-во купюр по 2: " + str(count2) +
#       "\nОстаток: " + str(sum2))

# # 13
# n_prost = int(input("Введите число: "))
# n = 2
# while n < n_prost:
#     if n_prost % n == 0:
#         print("Нет")
#         break
#         i += 1
#     elif n_prost < 2:
#         print("Введите число больше 1")
#     else:
#         print("Является")
#         break

# # 14
# M = int(input("Введите число М: "))
# a = int(input("Введите диапазон от а: "))
# b = int(input("Введите диапазон до b: "))
#
# for m in range(a, b+1):
#     res = M * m
#     print(str(M) + " * " + str(m) + " = " + str(res))

# # 15
# import random
# N = int(input("Введите длину:"))
# A = list(range(1, N+1))
# print(A)
# for i in range(len(A)-1):
#     A[i], A[i+1] = A[i+1], A[i]
# print(A)

# 16