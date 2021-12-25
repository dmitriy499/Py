def func_1(number):
    if number == 11:
        return print(f'{number} процентов')
    elif number % 10 == 1:
        return print(f'{number} процент')
    elif 12 <= number <=  14:
        return print(f'{number} процентов')
    elif 2 <= number % 10 <= 4:
        return print(f'{number} процента')
    else:
        return print(f'{number} процентов')
for i in range(101):
    func_1(i)