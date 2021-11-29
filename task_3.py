"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
mounths_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
                'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
seasons_list = ['зима', 'весна', 'лето', 'осень', 'зима']
mounths_dict = {'январь': 'зима', 'февраль': 'зима', 'март': 'весна', 'апрель': 'весна', 'май': 'весна',
                'июнь': 'лето', 'июль': 'лето', 'август': 'лето', 'сентябрь': 'осень', 'октябрь': 'осень',
                'ноябрь': 'осень', 'декабрь': 'зима'}
mounths_dict2 = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',  # 2-й способ
                 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}  # 2-й способ
seasons_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}  # 2-й способ
user_choice = input('Введите номер месяца >>> ')
if not user_choice.isdigit():
    print('Некорректный ввод данных')
    exit()
user_choice = int(user_choice)
if not 0 < user_choice < 13:
    print('Выбран несуществующий месяц')
    exit()
if 0 < user_choice < 3:  # 2-й способ
    season_list = seasons_list[0]  # 2-й способ
elif 2 < user_choice < 6:  # 2-й способ
    season_list = seasons_list[1]  # 2-й способ
elif 5 < user_choice < 9:  # 2-й способ
    season_list = seasons_list[2]  # 2-й способ
elif 8 < user_choice < 12:  # 2-й способ
    season_list = seasons_list[3]  # 2-й способ
else:  # 2-й способ
    season_list = seasons_list[0]  # 2-й способ
print(f'{mounths_list[user_choice -1]} {seasons_list[user_choice // 3]} через list 1-й способ')
print(f'{mounths_list[user_choice -1]} {season_list} через list 2-й способ')
print(f'{list(mounths_dict.items())[user_choice - 1]}  через dict 1-й способ')
print(f'{mounths_dict2.get(user_choice)} {seasons_dict.get(user_choice // 3)}  через dict 2-й способ')
