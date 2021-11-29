"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

"""
ratings = [None]
number_of_members = input('Введите кол-во участников >>> ')
if not number_of_members.isdigit():
    print('Некорректный ввод данных. Введите целое, положительное число')
    exit()
number_of_members = int(number_of_members)
check_passed = 0
counter = 0
for i in range(number_of_members):
    while check_passed == 0:
        member_rating = input('Введите рейтинг участника >>> ')
        if not member_rating.isdigit():
            print('Некорректный ввод данных. Введите целое, положительное число')
            continue
        else:
            check_passed = 1
            member_rating = int(member_rating)
            counter += 1
            if ratings[0] is None:
                ratings[0] = member_rating
            elif member_rating <= min(ratings):
                ratings.append(member_rating)
    for q in range(counter):
        if member_rating > ratings[q]:
            ratings.insert(q, member_rating)
            break
    check_passed = 0
    print(f'Рейтинг {ratings}')
"""

"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""

"""
number_of_members = input('Введите кол-во участников >>> ')
if not number_of_members.isdigit():
    print('Некорректный ввод данных. Введите целое, положительное число')
    exit()
number_of_members = int(number_of_members)
ratings = []
check_passed = 0
for i in range(number_of_members):
    while check_passed == 0:
        member_rating = input('Введите рейтинг участника >>> ')
        if not member_rating.isdigit():
            print('Некорректный ввод данных. Введите целое, положительное число')
            continue
        else:
            check_passed = 1
            member_rating = int(member_rating)
            ratings.append(member_rating)
            ratings.sort(reverse=True)
            print(f'Рейтинг {ratings}')
    check_passed = 0
"""

"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""


ratings = [None]  # список позиций в рейтинге
number_of_members = input('Введите кол-во результатов которые хотите внести >>> ')  # кол-во участников
if not number_of_members.isdigit():  # проаерко ввода
    print('Некорректный ввод данных. Введите целое, положительное число')
    exit()
number_of_members = int(number_of_members)
rating_members = [None]  # участники рейтинга
counter = 0  # счетчик циклов
while counter < number_of_members:  # Основной цикл
    member_rating = None  # рейтинг текущего(щей) участник(цы)
    check_passed = 0  # проверка пройденности цикла
    member = input('Введите имя участника >>> ')  # текущий(ая) участник(ца)
    while member_rating is None and check_passed == 0:  # ввод и проверка правильности ввода текущего рейтинга
        member_rating = input('Введите рейтинг участника >>> ')
        if not member_rating.isdigit():
            print('Некорректный ввод данных. Введите целое, полржительное число')
            continue
        else:
            check_passed = 1
            member_rating = int(member_rating)
            # проверка повторного ввода участника(цы)
        if member in rating_members and member_rating > ratings[rating_members.index(member)] and len(ratings) == 1:
            ratings, rating_members = [None], [None]
            # counter -= 1 # Необходимо дабавить, если откличили доп. блок
        if member in rating_members and member_rating > ratings[rating_members.index(member)] and len(ratings) > 1:
            ratings.pop(rating_members.index(member))
            rating_members.pop(rating_members.index(member))
            # counter -= 1 # Необходимо дабавить, если откличили доп. блок
        elif member in rating_members and member_rating == ratings[rating_members.index(member)]:
            print(f'{member} повторил(а) свой результат {member_rating} или результат введен повторно')
            # counter -= 1 # Необходимо дабавить, если откличили доп. блок
            continue
        elif member in rating_members and member_rating < ratings[rating_members.index(member)]:
            print(f'{member} показал(а) меньший результат {member_rating} или введен более ранний результат')
            # counter -= 1 # Необходимо дабавить, если откличили доп. блок
            continue
        # внесение данных
        for q in range(len(ratings)):
            if ratings[0] is None:
                ratings[0] = member_rating
                rating_members[0] = member
                counter += 1
                break
            elif member_rating <= min(ratings):
                ratings.append(member_rating)
                rating_members.append(member)
                counter += 1
                break
            elif member_rating > ratings[q]:
                ratings.insert(q, member_rating)
                rating_members.insert(q, member)
                counter += 1
                break

    print('Рейтинг')
    for a in range(len(ratings)):
        print(f'{ratings[a]}  {rating_members[a]}')
# ВНИМАНИЕ-ДОПОЛНИТЕЛЬНЫЙ БЛОК!!!!!!!!!!!!! Для решения задачи весь следующий блок не нужен
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if counter == number_of_members:
        choice = input('Хотите обновить данные? Нажмите n, y или ERASE, для очищения данных  и нового ввода >>> ')
        if choice == 'n':
            continue
        elif choice == 'y':
            while choice != number_of_members:
                choice = input('Введите кол-во результатов которые хотите внести,'
                               ' если передумали введите n >>> ')
                if choice == 'n':
                    choice = number_of_members
                elif not choice.isdigit():
                    print('Некорректный ввод данных. Введите целое, положительное число, если передумали введите n')
                    continue
                else:
                    choice = int(choice)
                    number_of_members = choice
                    counter = 0
        elif choice == 'ERASE':
            print('Вы точно уверены, что хотите обнулить рейтинг. ВСЕ ВВЕДЕННЫЕ РАНЕЕ ДАННЫЕ БУДУТ СТЕРТЫ.')
            while choice != number_of_members:
                choice = input('Если уверены введите "YES I WANT TO ERASE RATING", если педумали n >>> ')
                if choice == 'n':
                    choice = number_of_members
                elif choice == 'YES I WANT TO ERASE RATING':
                    number_of_members = None
                    while number_of_members is None:
                        number_of_members = input('Введите кол-во результатов которые хотите внести,'
                                                  ' если передумали введите n >>> ')
                        if not number_of_members.isdigit():
                            number_of_members = None
                            print('Некорректный ввод данных. Введите целое, положительное число, если передумали n')
                        else:
                            number_of_members = int(number_of_members)
                            ratings, rating_members = [None], [None]
                            choice = number_of_members
                            counter = 0
