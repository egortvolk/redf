from random import randint
from time import*
class Hero():
    def __init__(self, name, health, armor, power,armortime,armorpower, healtime,healpower,coins, weapon):
       self.name = name
       self.health = health
       self.armor = armor 
       self.power = power 
       self.weapon = weapon
       self.coins = coins
       self.armortime = armortime
       self.armorpower = armorpower
       self.healtime = healtime
       self.healpower = healpower
       self.new = True
    def print_info_hero(self):
       print('Уровень здоровья:', self.health)
       print('Класс брони:', self.armor)
       print('Сила пополнения жизней:', self.healpower)
       print('Ходов до активации зелья здоровья:', self.healtime)
       print('Сила пополнения брони:', self.armorpower)
       print('Ходов до активации брони', self.armortime)
       print('Монет',self.coins)

    def print_info_warrior(self):
       print('Уровень здоровья:', self.health)
       print('Класс брони:', self.armor)

    
    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def strike(self, enemy):
       enemy.armor -= self.power
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
 
class Warrior(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! Из глубины леса появляется искусный воин', self.name)
            self.new = False
        else:
            print('Снова появляется воинственный воин', self.name)

    def attack(self, enemy): 
        print(self.name, 'бесстрашно набрасывается на', enemy.name)
        print('используя ', self.weapon)
        print('Результат схватки для', self.name)
        self.print_info_warrior()
        print('Результат схватки для', enemy.name)
        enemy.print_info_warrior()

class Archer(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! Из глубины леса появляется искусный лучник', self.name)
            self.new = False
        else:
            print('Снова появляется воинственный лучник', self.name)

    def attack(self, enemy): 
        print(self.name, 'бесстрашно набрасывается на', enemy.name)
        print('используя ', self.weapon)
        print('Результат схватки для', self.name)
        self.print_info_warrior()
        print('Результат схватки для', enemy.name)
        enemy.print_info_warrior()

class Boss(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! Осторожно из глубины леса появляется босс', self.name)
            self.new = False
        else:
            print('Снова появляется сильный враг', self.name)
    
    def attack(self, enemy): 
        print(self.name, 'бесстрашно набрасывается на', enemy.name)
        print('используя ', self.weapon)
        print('Результат схватки для', self.name)
        self.print_info_warrior()
        print('Результат схватки для', enemy.name)
        enemy.print_info_warrior()
 
class Dragon(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! С неба спускается свирепый дракон', self.name)
            self.new = False
        else:
            print('И вновь перед нами разъярённый дракон', self.name)
    
    def attack(self, enemy): 
        print(self.name, 'нападает  на', enemy.name)
        print('используя поток смертельного', self.weapon)
        print('Результат схватки для', self.name)
        self.print_info_warrior()
        print('Результат схватки для', enemy.name)
        enemy.print_info_warrior()

name = input('Имя вашего рыцаря?')
print('От выбора оружия зависят все твои характеристики')
equipment = input('лук/меч/посох/секира/ ')
if equipment == 'лук' or equipment == '1':
    health1 = 50
    armor1 = 50
    damage1 = 70
    armortime1 = 5
    armorpower1 = 25
    healtime1 = 2
    healpower1 = 15
    coins1 = randint(0, 100)
elif equipment == 'секира' or equipment =="2":
    health1 = 250
    armor1 = 250
    damage1 = 75
    armortime1 =7
    armorpower1 =75
    healtime1 = 5
    healpower1 = 75
    coins1 = randint(0, 100)
elif equipment == 'меч'or equipment =="3":
    health1 = 100
    armor1 = 100
    damage1 = 50
    armortime1 =6
    armorpower1 =25
    healtime1 = 5
    healpower1 = 25
    coins1 = randint(0, 100)
elif equipment == 'посох'or equipment =="4":
    health1 = 25
    armor1 = 0
    damage1 = 25
    armortime1 = -1
    armorpower1 = 0
    healtime1 = 2
    healpower1 = 50
    coins1 = randint(0, 100)
else:
    health1 = 10
    armor1 = 0
    damage1 = 2
    armortime1 = -1
    armorpower1 = 0
    healtime1 = -1
    healpower1 = 0
    coins1 = 0

knight = Warrior(name, health1 ,armor1 , damage1, armortime1,armorpower1, healtime1, healpower1,coins1 , equipment)
print('Приветствуем тебя, храбрый  рыцарь', knight.name)
print('Ты был хорошим королем, но тебя сверг Спартак!!!')
print('Ты стоишь у входа в лес,который ведет тебя в твое королевство. Готов ли ты войти внутрь и сразиться с врагами (да/нет)?')
starttime = time()
answer = input()
if answer == 'да':
    knight.print_info_hero()
    play = True
    print('\n***Да начнётся битва!*** \n')
else:
    play = False
    endtime = time()
    stime = (endtime - starttime) // 1
    print('врямя  супер игры :(', stime)
 
enemies = list()
enemies.append(Archer('Питер',randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'лук'))
enemies.append(Warrior('Вася', randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'саблю'))
enemies.append(Warrior('Радивил',randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'булаву'))
enemies.append(Archer('Гоша', randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'лук'))
enemies.append(Warrior('Печкин', randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'молот'))
enemies.append(Warrior('Серый', randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'меч'))
enemies.append(Warrior('Витька', randint(10, 50) ,randint(10, 50), randint(5, 35),3, 25,5, 25,randint(0, 50) ,'секиру'))
enemies.append(Warrior('Сержио', 85, 15, 20,4, 50,5, 25,randint(0, 50) , 'меч'))
enemies.append(Dragon('Дрогон', 100, 25, 26,6, 50,7, 50,randint(0, 50) , 'льда'))
enemies.append(Dragon('Визерион', 50, 55, 30,5, 20,1, 10,randint(0, 50), 'огня'))
core = 0
admcore = 0
killed = 0
sell = 0
price = 25
powerweapon =15
while play:
    enemy = enemies[randint(0,len(enemies)-1)]
    enemy.hello()
    enemy.print_info_warrior()
 
    is_attack = input('Что будешь делать (1-атака/2-отступить/3-подлечить себя/\n 4-пополнить броню/5-улучшить оружие/?- узнать свои характеристики)?')
    is_attack =is_attack.lower()
    if is_attack == '?':
        print('характеристики', knight.name)
        knight.print_info_hero()
    if is_attack == '5':
        print('Денег',knight.coins)
        if knight.coins >= price:
            knight.coins -= price
            knight.power += powerweapon
            print('Сила',knight.power)
            price = 2 * price
            print('Цена', price)
        else:
            print('Вам не хватает',price - knight.coins,'монет')
    if is_attack == '3':
        if knight.healtime <= 0:
            knight.health += knight.healpower
            knight.healtime = healtime1 + 1
            print('Вы подняли себе HP до: ',knight.health)
        else:
            print('Перезарядка еще:', knight.healtime)

    if is_attack == '4':
        if knight.armortime <= 0:
            knight.armor += knight.armorpower
            knight.armortime = armortime1 + 1
            print('Вы подняли себе броню до:',knight.armor)
        else:
            print('Перезарядка еще:', knight.armortime)
    if is_attack == 'jwko2lx0kg2m0uq':
        enemies.remove(enemy)
        admcore += 1

    if is_attack == 'superhack':
        core += 1
        if core < 1:
            knight.power += 25
            print('Вы успешно активировали бонус код  :) ')  
        else:
            print('данный бонус-код использован') 

    if is_attack == '1': 
        knight.healtime -= 1
        knight.armortime -= 1
        if randint(0,1) == 1:
            figthers = [knight, enemy]
            figthers[0].strike(figthers[1])
            figthers[0].attack(figthers[1])
        else:
            if enemy.healtime <= 0:
                print(enemy.name,'испльзовал хилку')
                enemy.health += enemy.healpower
            elif enemy.armortime <= 0 and enemy.armor == 0:
                print(enemy.name,'испльзовал броньку')
                enemy.armor += enemy.armorpower
            else:
                enemy.armortime -= 1
                enemy.healtime -= 1
                figthers = [enemy, knight]
                figthers[0].strike(figthers[1])
                figthers[0].attack(figthers[1])
        
    print('---' * 6)
    if is_attack == 'конец' or is_attack == 'стоп':
        play = False
        endtime = time()
        print('Время игры:', (endtime - starttime) // 1)
    if enemy.check_alive() == False:
        print(enemy.name, 'погиб от руки', knight.name, '\n')
        knight.coins += enemy.coins
        enemies.remove(enemy)
        killed += 1
        knight.power += 5
        if  knight.health < 100:
            knight.health += knight.health//4
            if knight.health > 100:
                knight.armor += (knight.health - 100)
    if len(enemies) == 0  and sell == 0:
       sell += 1
       print('Ты победил всех преспешников, против тебя вышел ложе-король')
       enemies.append(Boss('Спартак', 200, 50, 35,3, 80,5, 25, randint(0, 50),'секиру'))
    if knight.check_alive() == False:
        print('Храбрый рыцарь', knight.name, 'погиб в бою с врагом:',enemy.name)
        play = False
        endtime = time()
        print('Увы, но ты проиграл.:( самое главное не сдавайся, пробуй еще раз!')
        stime = (endtime - starttime) // 1
        print('Время игры:', stime)
    if len(enemies) == 0:
        print('Храбрый рыцарь', knight.name, 'победил всех врагов!')
        play = False
        endtime = time()
        stime = (endtime - starttime) // 1
        if admcore > 0:
            print('Молодец!!! Ты вернул свое корролевство.\n хоть и с читами')
            print('Количество:',admcore)
        else:
            print('Молодец!!! Ты вернул свое корролевство.')  

        print('Время игры:',stime )
print('Тут сказка закончилась. ждите обновы')
