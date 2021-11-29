"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

from datetime import datetime

elements = [10, 0.9, 0b101, 0o15, 0x09af, 5 + 6j, "'1R!'", '', '''''', [1, 'A', 0 | 1], [], [[]],
            ('i', 1 + 1, 0 | 1), (), (()), {'242a^ba2va2=2'}, {1}, {None}, frozenset('1021)){{}}25010'),
            {1: None}, {None: 1}, {}, True, b'ki9', bytearray(b'ki9'), None, type(1), type(Exception),
            Exception, Exception(), Exception(SyntaxError), SyntaxError, datetime.now, datetime,
            datetime.now()]
for el in elements:
    print(f'{type(el)}   {el}')
