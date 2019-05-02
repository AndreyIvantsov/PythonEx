# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv  # pylint: disable=unbalanced-tuple-unpacking

txt = open(filename, 'r')
print('Содержимое файла %r:' % filename)
print(txt.read())
txt.close()

print('Введете имя файла снова:')
filename_again = input('> ')
txt_again = open(filename_again)
print(txt_again.read())
txt_again.close()
