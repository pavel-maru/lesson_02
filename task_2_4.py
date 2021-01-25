
# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# через рекурсию:

def sum(num, n):
    if n == 1:
        return num
    else:
        return num + sum((num / 2), (n - 1))

n = int(input('Введите количество элементов ряда: '))
num = 1

print(sum(num, n))

# через цикл:

n = int(input('Введите количество элементов ряда: '))
num = 1
sum = 0

for i in range(n):
    sum = sum + num
    num = num / 2

print(sum)
