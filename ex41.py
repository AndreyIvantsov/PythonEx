#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
# from urllib.request import urlopen
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Создается класс с именем %%%, наследующим %%%.",
    "class %%% (object):\n\tdef __init__ (self, ***)":
    "Класс %%% комбинирует __init__ с праметрами self, ***.",
    "class %%% (object):\n\tdef *** (self, @@@) ":
    "Класс комбинирует функцию с именем *** с параметрами self, @@@.",
    "*** = %%%() ":
    "Создается *** экземпляр класса %%%.",
    "***.*** (@@@) ":
    "Из *** получается функция ***, а затем вызывается с параметрами self, @@@.",
    "***.*** = '***'":
    "Из *** получается атрибут ***, а затем устанавливается равным '***'."
}

# тренировка запоминания фраз
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "russian":
    PHRASE_FIRST = True

# подгружаем словарь с сервера
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):

    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count('%%%'))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:

        result = sentence[:]

        # вымышленные имена классов
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # вымышленные прочие имена
        for word in other_names:
            result = result.replace("***", word, 1)

        # список вымышленных параметров
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# выполнение, пока не нажато сочетание клавиш CTRL+Z
try:
    while True:
        snippets = PHRASES.keys()
        # random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print(question)

            raw_input("> ")
            print("ОТВЕТ: %s\n\t" % answer)
except EOFError:
    print("Пока!")