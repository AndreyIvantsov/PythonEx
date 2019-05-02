# -*- coding: utf-8 -*-
from sys import argv

script, first, second, thrid = argv # pylint: disable=unbalanced-tuple-unpacking 

# Python 3
# $ python3 ex13.py Первая Вторая Третья
print('Этот сценарий называется: ', script)
print('Моя первая переменная называется: ', first)
print('Моя вторая переменная называется: ', second)
print('Моя третья переменная называется: ', thrid)

# Python 2
# $ python ex13.py Первая Вторая Третья
# print u'Этот сценарий называется: ', script
# print u'Моя первая переменная называется: ', first
# print u'Моя вторая переменная называется: ', second
# print u'Моя третья переменная называется: ', thrid