""""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
number_of_elements = input('Введите кол-во элементов в списке >>> ')
if not number_of_elements.isdigit():
    print('Некорректный ввод данных')
    exit()
number_of_elements = int(number_of_elements)
user_list = []
user_list_reversed = [None] * number_of_elements  # 2-вариант
#  user_list_reversed2 = [None] * number_of_elements  # если использовать без первого варианта, но можно и с ним
for q in range(number_of_elements):
    user_list.append(input(f'Введите {q + 1}-й элемент списка >>> '))
    if q % 2 != 0:  # 2-вариант
        user_list_reversed[q], user_list_reversed[q - 1] = user_list[q - 1], user_list[q]  # 2-вариант
        #  user_list_reversed2[q - 1] = input(f'Введите {q}-й элемент списка >>> ')
        #  user_list_reversed2[q] = input(f'Введите {q + 1}-й элемент списка >>> ')
        # если использовать без первого вариата
    elif q == number_of_elements - 1 and q % 2 == 0:  # 2-й вариант
        user_list_reversed[q] = user_list[q]  # 2-й вариант
        # user_list_reversed2[q] = input(f'Введите {q + 1}-й элемент списка >>> ')
        # если использовать без первого вариата
print(user_list)
for q in range(number_of_elements):
    if q % 2 == 0:
        continue
    else:
        user_list[q], user_list[q - 1] = user_list[q - 1], user_list[q]
print(user_list)
print(user_list_reversed)  # 2-вариант
