x = int(input('Введите время в секундах '))
day = x // 86400
hour = x // 3600 % 24
minute = x // 60 % 60
second = x % 60

if day == 0:
    print(hour, 'час.', minute, 'мин.', second, 'сек.')
elif day != 0 or hour == 0:
    print(minute, 'мин.', second, 'сек.')
else:
    print(day, 'дн.', hour, 'час.', minute, 'мин.', second, 'сек.')
