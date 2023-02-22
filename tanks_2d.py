from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#создаем ИГРОКА
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if tank.rect.x <= win_width-50 and tank.x_speed > 0 or tank.rect.x >= 0 and tank.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if tank.rect.y <= win_height-50 and tank.y_speed > 0 or tank.rect.y >= 0 and tank.y_speed < 0:
            self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

        platforms_touched = sprite.spritecollide(self, not_breakable_bar, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        platforms_touched = sprite.spritecollide(self, not_breakable_bar, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

        platforms_touched = sprite.spritecollide(self, waters, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)


        platforms_touched = sprite.spritecollide(self, waters, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        platforms_touched = sprite.spritecollide(self,box, True)

        platforms_touched = sprite.spritecollide(self, mines2, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.player_x= 123
                self.size_x = 123
                self.rect.top = max(self.rect.top, p.rect.bottom)
                
        platforms_touched = sprite.spritecollide(self, mines2, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                Player.player_x = 425
                Player.player_y =750
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                Player.player_x = 425
                Player.player_y = 750
                self.rect.left = max(self.rect.left, p.rect.right)


    def fire1(self):
        if down1 == True:
            if len(bullets1) < 5:
                bullet1 = Bulletdown('bull1.png', self.rect.centerx, self.rect.top, 7, 10, 10)
                bullets1.add(bullet1)
        if up1 == True:
            if len(bullets1) < 5:
                bullet1 = Bulletup('bull1.png', self.rect.centerx, self.rect.top, 7, 10, 10)
                bullets1.add(bullet1)
        if right1 == True:
            if len(bullets1) < 5:
                bullet1 = Bulletright('bull1.png', self.rect.centerx, self.rect.top, 10, 7, 10)
                bullets1.add(bullet1)
        if left1 == True:
            if len(bullets1) < 5:
                bullet1 = Bulletleft('bull1.png', self.rect.centerx, self.rect.top, 10, 7, 10)
                bullets1.add(bullet1)
    def shit1(self):
        if len(mines1) < 5:
            mine1 = Mine('mine.png',self.rect.centerx, self.rect.top, 15, 15,10)
            mines1.add(mine1)

class Player2(GameSprite):
    def __init__(self, player_image, player2_x, player2_y, size2_x, size2_y, player2_x_speed,player2_y_speed):
        GameSprite.__init__(self, player_image, player2_x, player2_y,size2_x, size2_y)

        self.x_speed2 = player2_x_speed
        self.y_speed2 = player2_y_speed

    def update(self):
        if tank2.rect.x <= win_width-50 and tank2.x_speed2 > 0 or tank2.rect.x >= 0 and tank2.x_speed2 < 0:
            self.rect.x += self.x_speed2
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed2 > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed2 < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if tank2.rect.y <= win_height-50 and tank2.y_speed2 > 0 or tank2.rect.y >= 0 and tank2.y_speed2 < 0:
            self.rect.y += self.y_speed2

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed2 > 0:
            for p in platforms_touched:
                self.y_speed2 = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed2 < 0:
            for p in platforms_touched:
                self.y_speed2 = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

        platforms_touched = sprite.spritecollide(self, not_breakable_bar , False)
        if self.x_speed2 > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed2 < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)


        platforms_touched = sprite.spritecollide(self, not_breakable_bar, False)
        if self.y_speed2 > 0:
            for p in platforms_touched:
                self.y_speed2 = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed2 < 0:
            for p in platforms_touched:
                self.y_speed2 = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        platforms_touched = sprite.spritecollide(self, waters , False)
        if self.x_speed2 > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed2 < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)


        platforms_touched = sprite.spritecollide(self, waters, False)
        if self.y_speed2 > 0:
            for p in platforms_touched:
                self.y_speed2 = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed2 < 0:
            for p in platforms_touched:
                self.y_speed2 = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        platforms_touched = sprite.spritecollide(self,box, True)

        platforms_touched = sprite.spritecollide(self, mines1, False)
        if self.y_speed2 > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed2 < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.player2_x= 123
                self.size2_x = 123
                self.rect.top = max(self.rect.top, p.rect.bottom)
                
        platforms_touched = sprite.spritecollide(self, mines1, False)
        self.player2_x = 150
        if self.x_speed2 > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
            self.player2_x = 50
        elif self.x_speed2 < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
            self.player2_x = 50
        



    def fire2(self):
        if down2 == True:
            if len(bullets2) < 5:
                bullet2 = Bulletdown('bull2.png', self.rect.centerx, self.rect.bottom, 7, 10, 10)
                bullets2.add(bullet2)
        if up2 == True:
            if len(bullets2) < 5:
                bullet2 = Bulletup('bull2.png', self.rect.centerx, self.rect.top, 7, 10, 10)
                bullets2.add(bullet2)
        if right2 == True:
            if len(bullets2) < 5:
                bullet2 = Bulletright('bull2.png', self.rect.centerx, self.rect.bottom, 10, 7, 10)
                bullets2.add(bullet2)
        if left2 == True:
            if len(bullets2) < 5:
                bullet2 = Bulletleft('bull2.png', self.rect.centerx, self.rect.bottom, 10, 7, 10)
                bullets2.add(bullet2)
    def shit2(self):
        if len(mines2) < 5:
            mine2 = Mine('mine.png',self.rect.centerx, self.rect.top, 15, 15,10)
            mines2.add(mine2)

#создаем  картинку
class Enemy3(GameSprite):
    side = 'down'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

#создаем пули
class Bulletdown(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height+5:
            self.kill()



class Bulletup(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = speed
    def update(self):                
        self.rect.y -= self.speed
        if self.rect.y < win_height - 905:
            self.kill()


class Bulletleft(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = speed
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < win_width-905:
            self.kill()

class Bulletright(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()

class Mine(GameSprite):
    def __init__(self, player_image, player3_x, player3_y, size3_x, size3_y, speed):
        GameSprite.__init__(self, player_image, player3_x, player3_y, size3_x, size3_y)
        self.speed = speed
    def update(self):                
        self.rect.y -= self.speed
#направление 
left1 = False
right1 = False
up1 = False
down1 = False

left2 = False
right2 = False
up2 = False
down2 = False





#создаем окно, размер, название 
win_width = 900
win_height = 900
display.set_caption('Tanks_2d')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('back.png'),(win_width, win_height))
 #создаем группы
barriers = sprite.Group()
waters = sprite.Group()
not_breakable_bar = sprite.Group() 
bush = sprite.Group()
box = sprite.Group()
bullets1 = sprite.Group()
bullets2 = sprite.Group()
mines1 = sprite.Group()
mines2 = sprite.Group()
enemys1 = sprite.Group()
enemys2 = sprite.Group()
#создаем и задаем стены
#создаем разрушаймые стены
#rnd=  randint(1 , 2)
rnd = 1
if rnd == 1: 
    #Создание стен
    wall1 = GameSprite('wall.png', 300, 0, 50, 50)
    wall2 = GameSprite('wall.png', 350, 0, 50, 50)
    wall3 = GameSprite('wall.png', 350, 50, 50, 50)

    wall4 = GameSprite('wall.png', 500, 0, 50, 50)
    wall5 = GameSprite('wall.png', 550, 0, 50, 50)
    wall6 = GameSprite('wall.png', 500, 50, 50, 50)

    wall7 = GameSprite('wall.png', 300, 850, 50, 50) 
    wall8 = GameSprite('wall.png', 350, 850, 50, 50) 
    wall9 = GameSprite('wall.png', 350, 800, 50, 50)

    wall10 = GameSprite('wall.png', 500, 850, 50, 50) 
    wall11 = GameSprite('wall.png', 550, 850, 50, 50) 
    wall12 = GameSprite('wall.png', 500, 800, 50, 50)


    wall13 = GameSprite('wall.png', 550, 350, 50, 50)
    wall14 = GameSprite('wall.png', 500, 80, 50, 50)
    wall15 = GameSprite('wall.png', 450, 650, 50, 50)

    wall16 = GameSprite('wall.png', 600, 425, 50, 50)
    wall17 = GameSprite('wall.png', 550, 425, 50, 50)
    wall18 = GameSprite('wall.png',500, 425, 50, 50)
    wall19 = GameSprite('wall.png',450, 425, 50, 50)
    wall20 = GameSprite('wall.png',400, 425, 50, 50)
    wall21 = GameSprite('wall.png',350, 425, 50, 50)
    wall22 = GameSprite('wall.png', 300, 425, 50, 50)
    wall23 = GameSprite('wall.png',250, 425, 50, 50)
    #создаем воду
    water1 = GameSprite('water.png', 0, 550, 50, 50)
    water2 = GameSprite('water.png', 0, 500, 50, 50)
    water3 = GameSprite('water.png', 0, 450, 50, 50)
    water4 = GameSprite('water.png', 0, 400, 50, 50)
    water5 = GameSprite('water.png', 0, 350, 50, 50)
    water6 = GameSprite('water.png', 0, 300, 50, 50)

    water7 = GameSprite('water.png', 50, 500, 50, 50)
    water8 = GameSprite('water.png', 50, 450, 50, 50)
    water9 = GameSprite('water.png', 50, 400, 50, 50)
    water10 = GameSprite('water.png', 50, 350, 50, 50)

    water11 = GameSprite('water.png', 100, 450, 50, 50)
    water12 = GameSprite('water.png', 100, 400, 50, 50)

    water13 = GameSprite('water.png', 850, 550, 50, 50)
    water14 = GameSprite('water.png', 850, 500, 50, 50)
    water15 = GameSprite('water.png', 850, 450, 50, 50)
    water16 = GameSprite('water.png', 850, 400, 50, 50)
    water17 = GameSprite('water.png', 850, 350, 50, 50)
    water18 = GameSprite('water.png', 850, 300, 50, 50)

    water19 = GameSprite('water.png', 800, 500, 50, 50)
    water20 = GameSprite('water.png', 800, 450, 50, 50)
    water21 = GameSprite('water.png', 800, 400, 50, 50)
    water22 = GameSprite('water.png', 800, 350, 50, 50)

    water23 = GameSprite('water.png', 750, 450, 50, 50)
    water24 = GameSprite('water.png', 750, 400, 50, 50)
    #правые нераз стены
    nw1 = GameSprite('not_breakable_bar.png',700, 450, 50, 50)
    nw2 = GameSprite('not_breakable_bar.png', 600, 450, 50, 50) 
    nw3 = GameSprite('not_breakable_bar.png', 650, 450, 50, 50)
    #левые нераз стены
    nw4 = GameSprite('not_breakable_bar.png', 250, 400, 50, 50)
    nw5 = GameSprite('not_breakable_bar.png', 150, 400, 50, 50)
    nw6 = GameSprite('not_breakable_bar.png',200, 400, 50, 50)
    
    

    #кусты
    bush1 = GameSprite('bush.png', 250, 350, 50, 50)
    bush2 = GameSprite('bush.png', 150, 350, 50, 50)
    bush3 = GameSprite('bush.png',200, 350, 50, 50)

    bush4 = GameSprite('bush.png', 700, 500, 50, 50)
    bush5 = GameSprite('bush.png', 600, 500, 50, 50)
    bush6 = GameSprite('bush.png',650, 500, 50, 50)

    # Корбки разрушаймые таранами и выстрелами
    box1 = GameSprite('box.png', 100, 100, 50,50)

    barriers.add(wall1)
    barriers.add(wall2)
    barriers.add(wall3)
    barriers.add(wall4)
    barriers.add(wall5)
    barriers.add(wall6)
    barriers.add(wall7)
    barriers.add(wall8)
    barriers.add(wall9)
    barriers.add(wall10)
    barriers.add(wall11)
    barriers.add(wall12)
    barriers.add(wall13)
    barriers.add(wall14)
    barriers.add(wall15)
    barriers.add(wall16)
    barriers.add(wall17)
    barriers.add(wall18)
    barriers.add(wall19)
    barriers.add(wall20)
    barriers.add(wall21)
    barriers.add(wall22)
    barriers.add(wall23)

    waters.add(water1)
    waters.add(water2)
    waters.add(water3)
    waters.add(water4)
    waters.add(water5)
    waters.add(water6)
    waters.add(water7)
    waters.add(water8)
    waters.add(water9)
    waters.add(water10)
    waters.add(water11)
    waters.add(water12)
    waters.add(water13)
    waters.add(water14)
    waters.add(water15)
    waters.add(water16)
    waters.add(water17)
    waters.add(water18)
    waters.add(water19)
    waters.add(water20)
    waters.add(water21)
    waters.add(water22)
    waters.add(water23)
    waters.add(water24)


    not_breakable_bar.add(nw1)
    not_breakable_bar.add(nw2)
    not_breakable_bar.add(nw3)
    not_breakable_bar.add(nw4)
    not_breakable_bar.add(nw5)
    not_breakable_bar.add(nw6)

    bush.add(bush1)
    bush.add(bush2)
    bush.add(bush3)
    bush.add(bush4)
    bush.add(bush5)
    bush.add(bush6)

    box.add(box1)
if rnd == 2:
#Кусты
    bush1 = GameSprite('bush.png', 350, 375, 50, 50)
    bush2 = GameSprite('bush.png', 150, 425, 50, 50)
    bush3 = GameSprite('bush.png', 150, 425, 50, 50)
#Кирпич
    wall1 = GameSprite('wall.png', 300, 0, 50, 50)
    wall2 = GameSprite('wall.png', 350, 0, 50, 50)
    wall3 = GameSprite('wall.png', 350, 50, 50, 50)

    wall4 = GameSprite('wall.png', 500, 0, 50, 50)
    wall5 = GameSprite('wall.png', 550, 0, 50, 50)
    wall6 = GameSprite('wall.png', 500, 50, 50, 50)

    wall7 = GameSprite('wall.png', 300, 850, 50, 50) 
    wall8 = GameSprite('wall.png', 350, 850, 50, 50) 
    wall9 = GameSprite('wall.png', 350, 800, 50, 50)

    wall10 = GameSprite('wall.png', 500, 850, 50, 50) 
    wall11 = GameSprite('wall.png', 550, 850, 50, 50) 
    wall12 = GameSprite('wall.png', 500, 800, 50, 50)


    #wall13 = GameSprite('wall.png', 550, 350, 50, 50)
    #wall14 = GameSprite('wall.png', 500, 80, 50, 50)
    #wall15 = GameSprite('wall.png', 300, 300, 50, 50)
# вода
    water1 = GameSprite('water.png', 0, 425, 50, 50)
    water2 = GameSprite('water.png', 50, 425, 50, 50)
    water3 = GameSprite('water.png', 100, 425, 50, 50)

    water4 = GameSprite('water.png', 200, 425, 50, 50)
    water5 = GameSprite('water.png', 250, 425, 50, 50)
    water6 = GameSprite('water.png', 300, 425, 50, 50)
    water7 = GameSprite('water.png', 350, 425, 50, 50)

    water8 = GameSprite('water.png', 500, 425, 50, 50)
    water9 = GameSprite('water.png', 550, 425, 50, 50)
    water10 = GameSprite('water.png', 600, 425, 50, 50)
    water11 = GameSprite('water.png', 650, 425, 50, 50)
    water12 = GameSprite('water.png', 750, 425,50 ,50)

    water13 = GameSprite('water.png',800 , 425, 50, 50)
    water14 = GameSprite('water.png', 850, 425, 50,50)


    barriers.add(wall1)
    barriers.add(wall2)
    barriers.add(wall3)
    barriers.add(wall4)
    barriers.add(wall5)
    barriers.add(wall6)
    barriers.add(wall7)
    barriers.add(wall8)
    barriers.add(wall9)
    barriers.add(wall10)
    barriers.add(wall11)
    barriers.add(wall12)
    #barriers.add(wall13)
    #barriers.add(wall14)
    #barriers.add(wall15)

    bush.add(bush1)
    bush.add(bush2)
    waters.add(water1)
    waters.add(water2)
    waters.add(water3)
    waters.add(water4)
    waters.add(water5)
    waters.add(water6)
    waters.add(water7)
    waters.add(water8)
    waters.add(water9)
    waters.add(water10)
    waters.add(water11)
    waters.add(water12)
    waters.add(water13)
    waters.add(water14)
#помещаем в группу стены



img_Player1 ='Player1.png'
img_Player2 ='Player2.png'
#создаем игрока, врагов и финал 
tank = Player(img_Player1, 425, win_height - 150, 50, 50, 0, 0)
tank2 = Player2(img_Player2, 425, win_height - 800, 50, 50, 0, 0)
enemy1_2 = Enemy3('Player1.png', win_width - 350, 500, 200, 200, 5)
enemy1 = Enemy3('Player1.png', win_width - 800, 500, 200, 200, 5)
enemy2_2 = Enemy3('Player2.png', win_width - 800, 500, 200, 200, 5)
enemy2 = Enemy3('Player2.png', win_width - 350, 500, 200, 200, 5)
final_sprite1 = GameSprite('base1.1.png', 400, win_height - 100, 100, 100)
final_sprite2 = GameSprite('base2.1.png', 400,  0, 100, 100)
#помещаем в группу врагов
enemys1.add(enemy1)
enemys1.add(enemy2)
enemys2.add(enemy1_2)
enemys2.add(enemy2_2)


# попытка создать анимацию

finish = False

run = True
#начало основного цикла
while run:
    time.delay(50)
#управление в игре
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            #нажатие клавишь
            if e.key == K_LEFT:
                tank2.x_speed2 = -5
                left2 = True
                right2 = False
                up2 = False
                down2 = False

            elif e.key == K_RIGHT:
                tank2.x_speed2 = +5
                left2 = False
                right2 = True
                up2 = False
                down2 = False                
                
            elif e.key == K_DOWN:
                tank2.y_speed2 = +5
                left2 = False
                right2 = False
                up2 = False
                down2 = True
            elif e.key == K_UP:
                tank2.y_speed2 = -5
                left2 = False
                right2 = False
                up2 = True
                down2 = False
            elif e.key == K_p:
                
                tank2.fire2()

            elif e.key == K_l:
                tank2.shit2()




            elif e.key == K_w:
                tank.y_speed = -5
                left1 = False
                right1 = False
                up1 = True
                down1 = False
            elif e.key == K_s:
                tank.y_speed = +5
                left1 = False
                right1 = False
                up1= False
                down1 = True
            elif e.key == K_a:
                tank.x_speed = -5
                left1 = True
                right1 = False
                up1 = False
                down1 = False
            elif e.key == K_d:
                tank.x_speed = +5
                left1 = False
                right1 = True
                up1 = False
                down1 = False
            elif e.key == K_SPACE:
                tank.fire1()
            elif e.key == K_e:
                tank.shit1()

 
        elif e.type == KEYUP:
            #отжатие клавишь
            if e.key == K_LEFT:
                tank2.x_speed2 = 0
            elif e.key == K_RIGHT:
                tank2.x_speed2 = 0
            elif e.key == K_DOWN:
                tank2.y_speed2 = 0
            elif e.key == K_UP:
                tank2.y_speed2 = 0

            if e.key == K_w:
                tank.y_speed = 0
            elif e.key == K_s:
                tank.y_speed = 0
            elif e.key == K_a:
                tank.x_speed = 0
            elif e.key == K_d:
                tank.x_speed = 0

    if not finish:
    #рисуем все
        window.blit(background, (0, 0))
 
        tank.update()
        tank2.update()
        bullets1.update()
        bullets2.update()
 
        waters.draw(window) 
        bullets1.draw(window)
        bullets2.draw(window)
        barriers.draw(window)
        not_breakable_bar.draw(window)
        box.draw(window)
        mines1.draw(window)
        mines2.draw(window)
        
        final_sprite1.reset()
        final_sprite2.reset()
        tank.reset()
        tank2.reset()  
        bush.draw(window)     
 


        sprite.groupcollide(bullets1, barriers, True, True)
        sprite.groupcollide(bullets1, not_breakable_bar, True, False)
        sprite.groupcollide(bullets2, barriers, True, True)
        sprite.groupcollide(bullets2, not_breakable_bar, True, False)


        if sprite.collide_rect(tank, tank2):
            tank = Player(img_Player1, 425, win_height - 150, 50, 50, 0, 0)
            tank2 = Player2(img_Player2, 425, win_height - 800, 50, 50, 0, 0)

        if sprite.collide_rect(tank, final_sprite2):
            finish = True
            img = image.load('final_screen.png')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))        
            enemys1.update()
            enemys1.draw(window)
        #победа второго
        if sprite.collide_rect(tank2, final_sprite1):
            finish = True
            img = image.load('final_screen.png')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))        
            enemys2.update()
            enemys2.draw(window)

 
    display.update()
