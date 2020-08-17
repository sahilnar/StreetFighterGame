import pygame
import random
import MAIN_GAME as game
pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

white = 255,255,255
red = 255,0,0
black = 0,0,0
color_1 = 128,184,168
YELLOW = (255,255,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(color_1)

        return image


class Player1(pygame.sprite.Sprite):
    idleFrame = []
    walkingFrame = []
    punchFrame = []
    kickFrame = []
    superPunch = []
    health = 450
    strength = 0

    def __init__(self):
        super().__init__()
        sprite = Spritesheet(player_1_Sprite)
        self.image = sprite.getImage(5,17,43,83)
        self.idleFrame.append(self.image)
        self.image = sprite.getImage(54, 18, 45, 81)
        self.idleFrame.append(self.image)
        self.image = sprite.getImage(104, 17, 45, 83)
        self.idleFrame.append(self.image)
        self.image = sprite.getImage(153, 16, 44, 84)
        self.idleFrame.append(self.image)

        self.image = sprite.getImage(204,23,45,77)
        self.walkingFrame.append(self.image)
        self.image = sprite.getImage(251, 19, 45, 81)
        self.walkingFrame.append(self.image)
        self.image = sprite.getImage(300, 16, 45, 84)
        self.walkingFrame.append(self.image)
        self.image = sprite.getImage(350, 19, 45, 81)
        self.walkingFrame.append(self.image)
        self.image = sprite.getImage(401, 18, 43, 82)
        self.walkingFrame.append(self.image)

        self.image = sprite.getImage(170, 133, 43, 83)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(218, 129, 51, 87)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(272, 130, 75, 86)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(218, 129, 51, 87)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(170, 133, 43, 83)
        self.punchFrame.append(self.image)

        self.image = sprite.getImage(194, 263, 45, 85)
        self.kickFrame.append(self.image)
        self.image = sprite.getImage(243, 260, 59, 86)
        self.kickFrame.append(self.image)
        self.image = sprite.getImage(305, 261, 72, 86)
        self.kickFrame.append(self.image)
        self.image = sprite.getImage(379, 273, 62, 74)
        self.kickFrame.append(self.image)
        self.image = sprite.getImage(447, 272, 45, 75)
        self.kickFrame.append(self.image)

        self.image = sprite.getImage(616, 531, 52, 83)
        self.superPunch.append(self.image)
        self.image = sprite.getImage(672, 537, 66, 77)
        self.superPunch.append(self.image)
        self.image = sprite.getImage(743, 542, 66, 73)
        self.superPunch.append(self.image)
        self.image = sprite.getImage(814, 543, 71, 72)
        self.superPunch.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 - 250, height / 2 + 70)
        self.moveX = 0

        self.pos = 0

        self.idle = True
        self.move = False
        self.punch = False
        self.kick = False
        self.spunch = False

    def update(self, *args):
        self.pos += 4
        self.hit = pygame.sprite.groupcollide(playerSprite1, playerSprite2, False, False)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_d]:
            self.moveX = 5
            self.move = True
            self.idle = False
            if self.hit:
                self.moveX = 0
                self.move = False
                self.idle = True
        elif keystate[pygame.K_a]:
            self.moveX = -5
            self.move = True
            self.idle = False
            self.kick = False
            self.spunch = False
            if self.rect.x < 50:
                self.move = False
                self.moveX = 0
                self.idle = True
        elif keystate[pygame.K_w]:
            self.idle = False
            self.punch = True
        elif keystate[pygame.K_s]:
            self.idle = False
            self.kick = True
        elif keystate[pygame.K_x]:
            self.idle = False
            self.kick = False
            self.spunch = True
        else:
            self.spunch = False
            self.move = False
            self.punch = False
            self.idle = True
            self.moveX = 0

        if self.idle:
            self.currentFrame = (self.pos // 30) % len(self.idleFrame)
            self.image = self.idleFrame[self.currentFrame]
        elif self.move:
            self.currentFrame = (self.pos // 20) % len(self.walkingFrame)
            self.image = self.walkingFrame[self.currentFrame]
        elif self.punch:
            self.currentFrame = (self.pos // 30) % len(self.punchFrame)
            self.image = self.punchFrame[self.currentFrame]
            if self.hit:
                player2.strength -= 1
        elif self.kick:
            self.currentFrame = (self.pos // 30) % len(self.kickFrame)
            self.image = self.kickFrame[self.currentFrame]
            if self.hit:
                player2.strength -= 2
        elif self.spunch:
            self.currentFrame = (self.pos // 30) % len(self.superPunch)
            self.image = self.superPunch[self.currentFrame]
            if self.hit:
                player2.strength -= 3

        self.rect.x += self.moveX
        img_w = self.image.get_width() * 3
        img_h = self.image.get_height() * 3
        self.image = pygame.transform.scale(self.image, (img_w , img_h))
        self.rect.width = img_w
        self.rect.height = img_h


player_1_Sprite = pygame.image.load("img/fighter_1.gif")

all_sprites = pygame.sprite.Group()
player1 = Player1()
playerSprite1 = pygame.sprite.Group()
playerSprite1.add(player1)
all_sprites.add(player1)


class Player2(pygame.sprite.Sprite):
    idleFrame = []
    walkingFrame = []
    punchFrame = []
    kickFrame = []
    superKick = []
    hit_frames = []
    cpu_moves = []
    health = 450
    strength = 0

    def __init__(self):
        super().__init__()
        sprite = Spritesheet(player_2_Sprite)
        self.image = sprite.getImage(2358, 40, 104, 226)
        self.idleFrame.append(self.image)
        self.image = sprite.getImage(2559, 36, 102, 230)
        self.idleFrame.append(self.image)
        self.image = sprite.getImage(2748, 38, 105, 229)
        self.idleFrame.append(self.image)

        self.image = sprite.getImage(2750, 41, 102, 226)
        self.walkingFrame.append(self.image)
        self.image = sprite.getImage(2756, 317, 110, 224)
        self.walkingFrame.append(self.image)
        self.image = sprite.getImage(2394, 315, 94, 226)
        self.walkingFrame.append(self.image)

        self.image = sprite.getImage(2737, 1219, 130, 238)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(2492, 1213, 184, 240)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(2492, 1213, 184, 240)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(2300, 1219, 130, 236)
        self.punchFrame.append(self.image)
        self.image = sprite.getImage(2108, 1225, 112, 232)
        self.punchFrame.append(self.image)

        self.image = sprite.getImage(1012, 905, 94, 228)
        self.kickFrame.append(self.image)
        self.image = sprite.getImage(811, 878, 135, 252)
        self.kickFrame.append(self.image)

        self.image = sprite.getImage(58, 217, 96, 267)
        self.superKick.append(self.image)
        self.image = sprite.getImage(216, 260, 136, 219)
        self.superKick.append(self.image)
        self.image = sprite.getImage(394, 332, 212, 118)
        self.superKick.append(self.image)
        self.image = sprite.getImage(646, 282, 92, 200)
        self.superKick.append(self.image)
        self.image = sprite.getImage(806, 365, 180, 111)
        self.superKick.append(self.image)
        self.image = sprite.getImage(1026, 300, 98, 258)
        self.superKick.append(self.image)

        # self.image = sprite.getImage(1174, 1571, 144, 242)
        # self.hit_frames.append(self.image)
        # self.image = sprite.getImage(1375, 1583, 123, 226)
        # self.hit_frames.append(self.image)

        self.cpu_moves.append(self.idleFrame)
        self.cpu_moves.append(self.punchFrame)
        self.cpu_moves.append(self.walkingFrame)
        self.cpu_moves.append(self.kickFrame)
        self.cpu_moves.append(self.superKick)

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 + 250, height / 2 + 170)

        self.idle = True
        self.move = False
        self.punch = False
        self.kick = False
        self.skick = False

        self.moveX = 0
        self.pos = 0
        self.changePos = 0
        self.random_frame = random.choice(self.cpu_moves)

    def update(self, *args):
        self.hit = pygame.sprite.groupcollide(playerSprite1, playerSprite2, False, False)
        self.pos += 1
        self.changePos += 1

        if self.changePos >= 60:
            self.changePos = 0
            self.random_frame = random.choice(self.cpu_moves)

        if self.changePos < 60:
            frame = (self.pos // 30) % len(self.random_frame)
            self.image = self.random_frame[frame]
            for i in range(len(self.walkingFrame)):
                if self.image == self.walkingFrame[i]:
                    self.moveX = -5
                    self.move = True
                    self.idle = False
                if self.hit:
                    self.moveX = 0
                    self.move = False
                    self.idle = True
            for i in range(len(self.idleFrame)):
                if self.image == self.idleFrame[i]:
                    self.idle = True
                    self.move = False
                    self.punch = False
                    self.kick = False
                    self.skick = False
            for i in range(len(self.kickFrame)):
                if self.image == self.kickFrame[i]:
                    self.kick = True
                    self.idle = False
                    self.punch = False
                    self.move = False
                    self.skick = False
            for i in range(len(self.punchFrame)):
                if self.image == self.punchFrame[i]:
                    self.punch = True
                    self.kick = False
                    self.idle = False
                    self.move = False
                    self.skick = False
            for i in range(len(self.superKick)):
                if self.image == self.superKick[i]:
                    self.skick = True
                    self.punch = False
                    self.kick = False
                    self.idle = False
                    self.move = False

        if self.idle:
            self.currentFrame = (self.pos // 30) % len(self.idleFrame)
            self.image = self.idleFrame[self.currentFrame]
        elif self.move:
            self.currentFrame = (self.pos // 30) % len(self.walkingFrame)
            self.image = self.walkingFrame[self.currentFrame]
        elif self.punch:
            self.currentFrame = (self.pos // 30) % len(self.punchFrame)
            self.image = self.punchFrame[self.currentFrame]
            if self.hit:
                player1.strength -= 1
        elif self.kick:
            self.currentFrame = (self.pos // 30) % len(self.kickFrame)
            self.image = self.kickFrame[self.currentFrame]
            if self.hit:
                player1.strength -= 2
        elif self.skick:
            self.currentFrame = (self.pos // 30) % len(self.superKick)
            self.image = self.superKick[self.currentFrame]
            if self.hit:
                player1.strength -= 3
        # elif self.isAttack:
        #     self.currentFrame = (self.pos // 30) % len(self.hit_frames)
        #     self.image = self.hit_frames[self.currentFrame]

        self.rect.x += self.moveX
        img_w = self.image.get_width()
        img_h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (img_w, img_h))
        self.image.set_colorkey(black)
        self.rect.width = img_w
        self.rect.height = img_h


pygame.time.set_timer(pygame.USEREVENT + 1, 1000)


def timer(seconds):
    font = pygame.font.Font('zorque.ttf', 40)
    seconds_display = font.render("Time Left: " + str(seconds), 1, GREEN)
    screen.blit(seconds_display, (width/2 - 130, 0))



def healthBarPlayer_1():
    health = 450+player1.strength

    if health > 300:
        col = GREEN
    elif health > 150:
        col = YELLOW
    else:
        col = RED

    if health < 0:
        gameOverScreen("2")

    pygame.draw.rect(screen, col, (10, 10, health, 40))


def healthBarPlayer_2():
    health = 450+player2.strength

    if health > 300:
        col = GREEN
    elif health > 150:
        col = YELLOW
    else:
        col = RED

    if health < 0:
        gameOverScreen("1")

    pygame.draw.rect(screen, col, (800, 10, health, 40))


player_2_Sprite = pygame.image.load("img/ryu_.png")

player2 = Player2()
playerSprite2 = pygame.sprite.Group()
playerSprite2.add(player2)
all_sprites.add(player2)


clock = pygame.time.Clock()
FPS = 100

splash_bg = pygame.image.load("img/k.png")
background = pygame.image.load("img/background.jpg")
# backgroundSound = pygame.mixer.Sound('snd/StreetFighter.ogg')

def gameOverScreen(x):
    running = True
    font = pygame.font.Font('zorque.ttf',60)
    text_1 = font.render("Game Over", True, white)
    text_2 = font.render("Player {} won".format(x), True, white)
    text_3 = font.render("Press Space to Start Again", True, white)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.blit(splash_bg, (0, 0))
                    startScreen()
                    splashScreen()

        screen.blit(text_1, (width/2 - 250, height/2 - 50))
        screen.blit(text_2, (width / 2 - 250, height / 2 - 150))
        screen.blit(text_3, (width / 2 - 350, height / 2 + 50))

        pygame.display.update()

    #pygame.quit()



def main():
    seconds = 10

    running = True
    player1.strength = 0
    player2.strength = 0

    while running:
        # backgroundSound.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT + 1:
                seconds -= 1
                # print(seconds)

        if seconds == -1:
            if player1.strength < player2.strength:
                gameOverScreen("2")
            elif player2.strength < player1.strength:
                gameOverScreen("1")


        screen.fill(white)
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        healthBarPlayer_1()
        healthBarPlayer_2()
        timer(seconds)
        # pygame.draw.rect(screen, black, player1.rect)
        # pygame.draw.rect(screen, black, player2.rect)
        pygame.display.update()
        clock.tick(FPS)


def startScreen():
    font = pygame.font.Font('zorque.ttf', 50)
    text_1 = font.render("Hit 1 to ", True, RED)
    text_2 = font.render("Start Game", True, RED)
    text_3 = font.render("MULTIPLAYER ", True, RED)
    text_4 = font.render("Hit 2 to ", True, RED)
    text_5 = font.render("Start Game", True, RED)
    text_6 = font.render("SINGLEPLAYER ", True, RED)
    screen.blit(text_1, (50,300))
    screen.blit(text_2, (50, 400))
    screen.blit(text_3, (50, 500))
    screen.blit(text_4, (900, 300))
    screen.blit(text_5, (900, 400))
    screen.blit(text_6, (900, 500))


def splashScreen():

    running = True
    player1.strength = 0
    player2.strength = 0
    pygame.display.update()
    # themeSound.play(-1)
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # themeSound.stop()
                    game.main()
                elif event.key == pygame.K_2:
                    # themeSound.stop()
                    main()


        screen.blit(splash_bg, (0, 0))
        startScreen()
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    splashScreen()
