"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods_number = input('Введите кол-во наименований товаров которые хотите внести >>> ')
if not goods_number.isdigit():  # проаерко ввода
    print('Некорректный ввод данных.')
    exit()
goods_number = int(goods_number)
goods = []
for i in range(goods_number):
    unit = input('Введите нименование товара >>> ')
    cost = None
    unit_number = None
    while cost is None:
        cost = input('Введите цену товара >>> ')
        if not cost.isdigit():
            print('Некорректный ввод данных. Введите целое, полржительное число')
            cost = None
        else:
            cost = int(cost)
    while unit_number is None:
        unit_number = input('Введите кол-во товара >>> ')
        if not unit_number.isdigit():
            print('Некорректный ввод данных. Введите целое, полржительное число')
            unit_number = None
        else:
            unit_number = int(unit_number)
    temp_dict = {'название': unit, 'цена': cost, 'количество': unit_number, 'eд': 'шт.'}
    temp_list = [i + 1, temp_dict]
    print(f'Введено {temp_list}')
    temp_tuple = tuple(temp_list)
    goods.append(temp_tuple)
print('Вы ввели список товаров')
for q in range(len(goods)):
    print(goods[q])
choice = None
while choice is None:
    choice = input('Свормировать аналитику? Нажмите y или n >>> ')
    if choice == 'n':
        exit()
    elif choice == 'y':
        continue
    else:
        choice = None
temp_list_units = []
temp_list_costs = []
temp_list_numbers = []
for i in range(goods_number):
    temp_tuple = goods[i]
    temp_dict = dict(temp_tuple[1])
    temp_list_units.append(temp_dict.get('название'))
    temp_list_costs.append(temp_dict.get('цена'))
    temp_list_numbers.append(temp_dict.get('количество'))
Statistics = {}
Statistics.update({'название': temp_list_units})
Statistics.update({'цена': temp_list_costs})
Statistics.update({'количество': temp_list_numbers})
Statistics.update({'ед': ['шт.']})
for key, value in Statistics.items():
    print(key, ':', value)
