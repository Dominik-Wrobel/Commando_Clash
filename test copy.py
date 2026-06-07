import pygame

pygame.init()
pygame.joystick.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((300, 300))

player1Input = ["Keyboard", 0]
player2Input = ["Keyboard", 0]

numJoysticks = 0


def myfunc1(isKeyboard):
    global player1Input
    global player2Input
    global numJoysticks
     
    if isKeyboard:
        player1Input = ["Keyboard", 0]
        numJoysticks = player2Input[1]
    elif player1Input[0] == "Keyboard" and len([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]) > numJoysticks:
        player1Input = ["Controller", player2Input[1] + 1]
        numJoysticks += 1
    print(f"Num joysticks:{numJoysticks}")
    print(player1Input)
    #print(len([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]))

def myfunc2(isKeyboard):
    global player1Input
    global player2Input
    global numJoysticks
    
    if isKeyboard:
        player2Input = ["Keyboard", 0]
        numJoysticks = player1Input[1]
    elif player2Input[0] == "Keyboard" and len([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]) > numJoysticks:
        player2Input = ["Controller", player1Input[1] + 1]
        numJoysticks += 1
    print(f"Num joysticks:{numJoysticks}")
    print(player2Input)
    #print(len([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]))

while True:
    CLOCK.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myfunc2(True)
            if event.key == pygame.K_p:
                myfunc2(False)
            if event.key == pygame.K_e:
                myfunc1(True)
            if event.key == pygame.K_r:
                myfunc1(False)
    pygame.display.update()