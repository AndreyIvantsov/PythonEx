# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv # pylint: disable=unbalanced-tuple-unpacking 
prompt = '>'

print('Привет %s, Я - сценарий %r.' % (user_name, script))
print('Я хочу задать тебе несколько вопросов.')
likes = input('%s Я тебе нравлюсь, %s? ' % (prompt, user_name))
lives = input('%s Где Вы живете, %s? ' % (prompt, user_name))
computer = input('%s На каком кампьютере Вы работаете, %s? ' %
                (prompt, user_name))

print("""
И так, Вы ответила %r на вопрос, нравлюсь ли я Вам.
Вы живете в %r. Не представляю где это.
И у Вас есть компьютер %r. Прекрасно!
""" % (likes, lives, computer))
