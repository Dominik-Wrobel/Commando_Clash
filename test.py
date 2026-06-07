import pygame

pygame.init()

class Player1:
    def __init__(self, pCurrentCharacter):
        if pCurrentCharacter == "Etai":
            self.player = Etai1()
        elif pCurrentCharacter == "Tane":
            self.player = Tane1()
        elif pCurrentCharacter == "Neor":
            self.player = Neor1()


class Player2:
    def __init__(self, pCurrentCharacter):
        if pCurrentCharacter == "Etai":
            self.player = Etai2()
        elif pCurrentCharacter == "Tane":
            self.player = Tane2()
        elif pCurrentCharacter == "Neor":
            self.player = Neor2()


class Etai1():
    def __init__(self, SCREEN):
        # Player health
        self.health = 1100
        self.image = pygame.image.load("Images/players/etai_1_model.png").convert_alpha(SCREEN)
        self.image = pygame.transform.scale(self.image, (SCREEN.get_width() / 7, SCREEN.get_height() / 5))
        self.rect = self.image.get_rect()
        # Move player 1 to the bottom left of the screen
        self.rect.bottomleft = (0,0)

class Etai2():
    def __init__(self, SCREEN):
        # Player health
        self.health = 1100
        self.image = pygame.image.load("Images/players/etai_2_model.png").convert_alpha(SCREEN)
        self.image = pygame.transform.scale(self.image, (SCREEN.get_width() / 7, SCREEN.get_height() / 5))
        self.rect = self.image.get_rect()
        # Move player 2 to the bottom right of the screen
        self.rect.bottomright = (SCREEN.get_width(), SCREEN.get_height())        

class Tane1():
    pass
class Tane2:
    pass
class Neor1:
    pass
class Neor2:
    pass