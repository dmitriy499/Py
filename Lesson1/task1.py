while True:
    duration = int(input('Введите время в секундах: '))
    d = duration // 86400 % 31
    h = duration // 3600 % 24
    m = duration // 60 % 60
    s = duration % 60
    print(f'{d} день, {h} час, {m} мин, {s} сек')

