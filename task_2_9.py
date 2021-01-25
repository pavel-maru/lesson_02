
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def f_sum(num): # функция считает сумму цифр в числе
    sum = 0
    length = len(num)
    # print(length)
    num = int(num)
    # print(num)
    for i in range(length):
        # print(i)
        digit = num % 10 ** (i +1) // 10 ** (i)
        # print(digit)
        sum = sum + digit
        # print(sum)
    return sum

# print(f_sum('956'))

num = '0'
sum = 0
while True:

    num2 = input('введите натуральное число (Q для выхода): ')

    if num2.lower() == 'q':
        break

    sum2 = f_sum(num2)
    # print(sum, sum2)
    # print(num, type(num), num2, type(num2))

    if sum < sum2:
        sum = sum2
        num = num2

    print(f'Из введённых чисел максимальную сумму имеет {num}; \n'
          f'сумма его цифр: {sum}.')
