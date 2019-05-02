# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv  # pylint: disable=unbalanced-tuple-unpacking

print('Копирование данных из файла %r в файл %r...' % (from_file, to_file))
in_file = open(from_file)
in_data = in_file.read()
print('Размер исходного файла %d байт.' % len(in_data))

print('Файл назначения существует - %r.' % exists(to_file))
input('Для продолжения нажмите ENTER, для отмены CTRL+C ')
out_file = open(to_file, 'w')
out_file.write(in_data)

in_file.close()
out_file.close()
print('Копирование завершено!')
