#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song([
    'Не могу я тебе в день рождения',
    'Дорогие подарки дарить',
    'Но зато в эти ночи весенние\n'
])

bulls_on_parade = Song([
    'Далеко-далеко на лугу пасется кто?!',
    'Пейте, дети, молоко, будете здоровы!\n'
])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
