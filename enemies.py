# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def IsPrime(n): #Проверяет простое ли число
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def Decomposition(n): #Раскладывает на простые множители
    res = []
    i = 2
    while IsPrime(n) == 0:
        if IsPrime(i) == 1 and n % i == 0:
            n = int(n / i)
            res.append(i)
            i = 2
        i += 1
    res.append(n)
    res.sort
    return (res[:-1])



def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

    def get_answer(self):
        return self.__answer

    def __str__(self):
        return "dragon"


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 30
        self._attack = 15
        self._color = 'красный'

    def question(self):
        x = randint(1,50)
        y = randint(1,50)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 25
        self._attack = 20
        self._color = 'чёрный'

    def question(self):
        x = randint(1,50)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

    def get_answer(self):
        return self.__answer

    def __str__(self):
        return "troll"


class BlueTroll(Troll):
    def __init__(self):
        self._health = 20
        self._attack = 10
        self._color = 'синий'

    def question(self):
        x = randint(1,3)
        self.__quest = "Угадай число от 1 до 3"
        self.set_answer(x)
        return self.__quest


class WhiteTroll(Troll):
    def __init__(self):
        self._health = 40
        self._attack = 15
        self._color = 'белый'

    def question(self):
        x = randint(2,100)
        self.__quest = 'Является ли число ' + str(x) + ' простым?(Введите 1 если да, 0 если нет)'
        if IsPrime(x):
            self.set_answer(True)
        else:
            self.set_answer(False)
        return self.__quest


enemy_types=[BlueTroll, WhiteTroll, GreenDragon, RedDragon, BlackDragon]
