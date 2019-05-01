# -*- coding: utf-8 -*-
my_name = 'Андрей'
my_age = 47         # лет
my_height = 178     # см
my_weight = 76      # кг
my_eyes = 'Карие'
my_teeth = 'Белые'
my_hair = 'Русые'

print('Давайте погворим о человеке по имени %s' %my_name)
print('Его рост составляет %d см.' %my_height)
print('Он весит %d кг.' %my_weight)
print('На самом деле это не так много.')
print('У него глаза %s и волосы %s.' %(my_eyes, my_hair))
print('Его зубы обычно %s, хотя он любит пить кофе.' %my_teeth)

# эта строка довольно сложная, не ошибитесь!

print('Если я сложу %d, %d и %d, то получу %d' %(my_age, my_height, my_weight, my_age + my_height + my_weight))

# --------------------------------------------------------------------------------------------- #
#   Формат          Что плучится                                                                #
# --------------------------------------------------------------------------------------------- #
#   '%d', '%i', '%u'  Десятичное число                                                          #
#   '%o'              Число в восьмиричной системе счисления                                    #
#   '%x'              Число в шестнадцатиричной системе счисления (буквы в нижнем регистре)     #
#   '%X'              Число в шестнадцатиричной системе счисления (буквы в верхнем ренистре)    #
#   '%e'              Число с плавающей точкой экспонентой (буквы в нижнем регистре)            #
#   '%E'              Число с плавающей точкой экспонентой (буквы в верхнем регистре)           #
#   '%f', '%F'        Число с плавающей точкой (обычный формат)                                 #
#   '%g'              Число с плавающей точкой с экспонентой (экспонента в нижнем регистре)     #
#   '%G'              Число с плавающей точкой с экспонентой (экспонента в верхнем регистре)    #
#   '%c'              Символ (строка из одного символа или число - код символа)                 #
#   '%r'              Строка (литерал python)                                                   #
#   '%s'              Строка (как обычно воспринимается пользователем)                          #
#   '%%'              Знак '%'                                                                  #
# --------------------------------------------------------------------------------------------- #
#
#
#
#