# Задание 1:
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# Задание 2:
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}','"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)


# Задание 4:
bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер Марина', "токарь высшего разряда Николай",
           "директор Аэлита"]
for position in bad_list:
    print('Привет', position.split()[-1].title())

# Задание 5:
goods = [58.7, 46.51, 98, 15, 34.56, 59.34, 2341, 7023]
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

goods = [58.7, 46.51, 98, 15, 34.56, 59.34, 2341, 7023]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп' , end=', ')