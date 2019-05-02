# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv  # pylint: disable=unbalanced-tuple-unpacking

print('Я собираюсь стереть файл %r.' % filename)
print('Если Вы не хотите его стирать, нажмите сочетание клавиж CTRL+C (^C).')
print('Если хотите стереть этот файл, нажмите ENTER.')
input('? ')

print('Открытие файла...')
target = open(filename, 'w')

print('Очистка  файла...')
target.truncate()

print('Теперь я запрашу у Вас три строчки:')
line1 = input('Строка 1: ') + '\n'
line2 = input('Строка 2: ') + '\n'
line3 = input('Строка 3: ')

print('Эти строки я запишу в файл %r...' % filename)
target.write(line1)
target.write(line2)
target.write(line3)
print('Я закрою файл %r...' % filename)
target.close()

print('Снова открою и выведу содержимое файла %r на экран...' % filename)
target = open(filename, 'r')
print(target.read())

print('Я закрою файл %r...' % filename)
target.close()

print('Работа окончена!')
