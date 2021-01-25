
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = input('Введите натуральное число: ')
length = len(num)
num = int(num)
num_res = 0

for i in range(length):
    digit = num % 10 ** (i +1) // 10 ** (i)
    num_res = num_res + digit * 10 ** (length - i - 1)
    # print(num, digit, num_res)

print(num_res)
