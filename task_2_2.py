
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')
length = len(num)
num = int(num)
even = 0
not_even = 0

for i in range(length):
    digit = num % 10 ** (i +1) // 10 ** (i)
    # print(digit)
    if digit % 2 == 0:
        even += 1
        # print('even', even)
    else:
        not_even += 1
        # print('not even', not_even)

print(f'чётных цифр: {even}, нечётных цифр: {not_even}')
