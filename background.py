import pygame

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, SCREEN):
        pygame.sprite.Sprite.__init__(self)

        self.backgroundWidth = SCREEN.get_width()
        self.backgroundHeight = SCREEN.get_height()

        self.expanded = False
    def update(self, SCREEN, player1pos, player2pos):
        SCREEN.blit(self.background, self.backgroundRect)
        SCREEN.blit(self.floor, self.floorRect)



class ColosseumMap(Background):
    def __init__(self, SCREEN):
        super().__init__(SCREEN)

        # Background
        self.background = pygame.image.load("Images/backgrounds/colosseum.png").convert_alpha(SCREEN)
        self.background = pygame.transform.scale(self.background, (self.backgroundWidth, self.backgroundHeight))

        self.backgroundRect = self.background.get_rect()

        self.backgroundRect.center = (SCREEN.get_width() / 2, 0)
        self.backgroundRect.bottom = SCREEN.get_height()

        # Floor
        self.floor = pygame.image.load("Images/backgrounds/colosseum_floor.png").convert_alpha(SCREEN)
        self.floor = pygame.transform.scale(self.floor, (self.backgroundWidth, self.backgroundHeight / 11))

        self.floorRect = self.floor.get_rect()

        self.floorRect.center = (SCREEN.get_width() / 2, 0)
        self.floorRect.bottom = SCREEN.get_height()
    def GetFloorBoundary(SCREEN):
        return SCREEN.get_height() * 2/11

class TundraMap(Background):
    def __init__(self, SCREEN):
        super().__init__(SCREEN)

        # Background
        self.background = pygame.image.load("Images/backgrounds/tundra.png").convert_alpha(SCREEN)
        self.background = pygame.transform.scale(self.background, (self.backgroundWidth, self.backgroundHeight))

        self.backgroundRect = self.background.get_rect()

        self.backgroundRect.center = (SCREEN.get_width() / 2, 0)
        self.backgroundRect.bottom = SCREEN.get_height()

        # Floor
        self.floor = pygame.image.load("Images/backgrounds/tundra_floor.png").convert_alpha(SCREEN)
        self.floor = pygame.transform.scale(self.floor, (self.backgroundWidth, self.backgroundHeight / 11))

        self.floorRect = self.floor.get_rect()

        self.floorRect.center = (SCREEN.get_width() / 2, 0)
        self.floorRect.bottom = SCREEN.get_height()
    def GetFloorBoundary(SCREEN):
        return SCREEN.get_height() * 2/11


class ClockworkMap(Background):
    def __init__(self, SCREEN):
        super().__init__(SCREEN)

        # Background
        self.background = pygame.image.load("Images/backgrounds/clockwork.png").convert_alpha(SCREEN)
        self.background = pygame.transform.scale(self.background, (self.backgroundWidth, self.backgroundHeight))

        self.backgroundRect = self.background.get_rect()

        self.backgroundRect.center = (SCREEN.get_width() / 2, 0)
        self.backgroundRect.bottom = SCREEN.get_height()

        # Floor
        self.floor = pygame.image.load("Images/backgrounds/clockwork_floor.png").convert_alpha(SCREEN)
        self.floor = pygame.transform.scale(self.floor, (self.backgroundWidth, self.backgroundHeight / 11))

        self.floorRect = self.floor.get_rect()

        self.floorRect.center = (SCREEN.get_width() / 2, 0)
        self.floorRect.bottom = SCREEN.get_height()
    def GetFloorBoundary(SCREEN):
        return SCREEN.get_height() * 2/11

class WarterMap(Background):
    def __init__(self, SCREEN):
        super().__init__(SCREEN)

        # Background
        self.background = pygame.image.load("Images/backgrounds/warter.png").convert_alpha(SCREEN)
        self.background = pygame.transform.scale(self.background, (self.backgroundWidth, self.backgroundHeight))

        self.backgroundRect = self.background.get_rect()

        self.backgroundRect.center = (SCREEN.get_width() / 2, 0)
        self.backgroundRect.bottom = SCREEN.get_height()

        # Floor
        self.floor = pygame.image.load("Images/backgrounds/warter_floor.png").convert_alpha(SCREEN)
        self.floor = pygame.transform.scale(self.floor, (self.backgroundWidth, self.backgroundHeight / 11))

        self.floorRect = self.floor.get_rect()

        self.floorRect.center = (SCREEN.get_width() / 2, 0)
        self.floorRect.bottom = SCREEN.get_height()
    def GetFloorBoundary(SCREEN):
        return SCREEN.get_height() * 2/11