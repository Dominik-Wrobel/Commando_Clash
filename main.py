import pygame
import menus
import background
from players import Etai, Tane, Neor

pygame.init()

SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
CLOCK = pygame.time.Clock()

# Main class
class main:
    global SCREEN
    global CLOCK

    def StartMenu(): 
        mainMenu = menus.MainMenu(SCREEN)
        #background = Background(SCREEN)

        running = True
        while running:
            CLOCK.tick(60)

            mainMenu.DrawMenu(SCREEN)
            currentEvent = mainMenu.RegisterInputs()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentEvent = -1
                    running = False
            if currentEvent:
                pygame.image.save(SCREEN, "myMainMenuScreenShot.png")
                running = False
            
            pygame.display.update()

        return currentEvent

    def StartRoundOptions():

        # Potential player names: Etai, Tane and Neor
        player1Name = ""
        player2Name = ""

        # Potential maps to be selected: Colosseum, Ice, Clock, Water
        selectedMap = ""
        
        RoundMenu = menus.RoundSettings(SCREEN)
        running = True

        player1Ready = False
        player2Ready = False

        player1Input = ["Keyboard", 0]
        player2Input = ["Keyboard", 0]

        numJoysticks = 0

        SCREEN.fill("black")
        while running:
            dt = CLOCK.tick(60) / 1000
            
            RoundMenu.BlitEffect(SCREEN, player1Name, player2Name)
            RoundMenu.BlitRoundSettings(SCREEN, player1Input[0], player2Input[0])
            currentEvent = RoundMenu.RegisterInputs()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentEvent = -1

            if currentEvent:
                match(currentEvent):
                    case 1:
                        currentEvent = 0
                        running = False
                    case 2:
                        player1Name = "Etai"
                    case 3:
                        player1Name = "Tane"
                    case 4:
                        player1Name = "Neor"
                    case 5:
                        player2Name = "Etai"
                    case 6:
                        player2Name = "Tane"
                    case 7:
                        player2Name = "Neor"
                    case 8:
                        if player1Name != "":
                            player1Ready = True
                            RoundMenu.ActivateReadyButton(True)
                    case 9:
                        if player2Name != "":
                            player2Ready = True
                            RoundMenu.ActivateReadyButton(False)
                    case 10:
                        selectedMap = "Colosseum"
                    case 11:
                        selectedMap = "Tundra"
                    case 12:
                        selectedMap = "Clockwork"
                    case 13:
                        selectedMap = "Warter"
                    case 14:
                        player1Input = ["Keyboard", 0]
                        numJoysticks = player2Input[1]
                    case 15:
                        if player1Input[0] == "Keyboard" and len([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]) > numJoysticks:
                            player1Input = ["Controller", player2Input[1] + 1]
                            numJoysticks += 1
                    case 16:
                        player2Input = ["Keyboard", 0]
                        numJoysticks = player1Input[1]
                    case 17:
                        if player2Input[0] == "Keyboard" and len([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]) > numJoysticks:
                            player2Input = ["Controller", player1Input[1] + 1]
                            numJoysticks += 1
                    case _:
                        running = False

            if player1Ready and player2Ready and player1Name != "" and selectedMap != "":
                currentEvent = 2
                running = False

            pygame.display.update()

        return currentEvent, player1Name, player2Name, selectedMap, player1Input, player2Input

    def StartRound(player1Name, player2Name, selectedMap, player1Input, player2Input):
        match(player1Name):
            case "Etai":
                player1 = Etai(SCREEN, True, player1Input)
            case "Tane":
                player1 = Tane(SCREEN, True, player1Input)
            case "Neor":
                player1 = Neor(SCREEN, True, player1Input)
            case _:
                print("ERROR!")
        match(player2Name):
            case "Etai":
                player2 = Etai(SCREEN, False, player2Input)
            case "Tane":
                player2 = Tane(SCREEN, False, player2Input)
            case "Neor":
                player2 = Neor(SCREEN, False, player2Input)
            case _:
                print("ERROR!")

        match(selectedMap):
            case "Colosseum":
                currentMap = background.ColosseumMap(SCREEN)
            case "Tundra":
                currentMap = background.TundraMap(SCREEN)
            case "Clockwork":
                currentMap = background.ClockworkMap(SCREEN)
            case "Warter":
                currentMap = background.WarterMap(SCREEN)
        
        running = True

        moveNotHit = True

        player1hit = False
        player2hit = False

        displayCooldown = 0

        while running == True:
            # Getting delta time for consistent framerates
            dt = CLOCK.tick(60) / 1000

            # Rendering
            keysPressed = pygame.key.get_pressed()

            if moveNotHit:

                if player1.isBlocking:
                    player1.isBlocking = False
                if player2.isBlocking:
                    player2.isBlocking = False

                if player1.isNotAttacking:
                    player1.update(SCREEN, dt)
                    if not player1.stunned:
                        player1.MovePlayer(keysPressed, dt)
                        player1CurrentMove = player1.RegisterMoves(keysPressed)
                        player1.ManageGauge()
                        player1.DisplayGauge(SCREEN)
                    else:
                        if pygame.time.get_ticks() >= player1.stunTime:
                            player1.stunned = False
                            player1.RotateSelf(False)

                if player2.isNotAttacking:
                    player2.update(SCREEN, dt)
                    if not player2.stunned:
                        player2.MovePlayer(keysPressed, dt)
                        player2CurrentMove = player2.RegisterMoves(keysPressed)
                    else:
                        if pygame.time.get_ticks() >= player2.stunTime:
                            player2.stunned = False
                            player2.RotateSelf(False)

                if player1CurrentMove and player1.isNotAttacking and pygame.time.get_ticks() >= player1.cooldownAttacks[player1CurrentMove]:
                    player1hit = player1.PerfomMove(player1CurrentMove, player2)
                    player1.ManageGauge()
                    player1.DisplayGauge(SCREEN)
                    player1.isNotAttacking = False
                    player1.displayCooldown = pygame.time.get_ticks() + 250

                if player2CurrentMove and player2.isNotAttacking and pygame.time.get_ticks() >= player2.cooldownAttacks[player2CurrentMove]:
                    player2hit = player2.PerfomMove(player2CurrentMove, player1)
                    player2.ManageGauge()
                    player2.DisplayGauge(SCREEN)
                    player2.isNotAttacking = False
                    player2.displayCooldown = pygame.time.get_ticks() + 250

                # Checking to see if both players' attacks hit at the same time
                if player1hit and player2hit:
                    player1hit = False
                    player2hit = False
                elif player1hit:
                    if player2.isBlocking:
                        pass
                    else:
                        player2.health -= player1.GetAttackDamage(player1CurrentMove)
                        player2.ManageHealth()
                        print(player2.health)
                        player1hit = False
                        player2.stunned = True
                        player2.stunTime = player1.GetAttackStunTime(player1CurrentMove)
                        player2.RotateSelf(True)
                        moveNotHit = False
                        displayCooldown = pygame.time.get_ticks() + 500
                elif player2hit:
                    if player1.isBlocking:
                        pass
                    else:
                        player1.health -= player2.GetAttackDamage(player2CurrentMove)
                        player1.ManageHealth()
                        player2hit = False
                        player1.stunned = True
                        player1.stunTime = player2.GetAttackStunTime(player2CurrentMove)
                        player1.RotateSelf(True)
                        moveNotHit = False
                        displayCooldown = pygame.time.get_ticks() + 500
            else:
                if pygame.time.get_ticks() >= displayCooldown:
                    moveNotHit = True
                    player1.isNotAttacking = True
                    player2.isNotAttacking = True

            #print(player1.rect.center)
            #print(player2.rect.center)
            #print(SCREEN.get_width())
            #print(SCREEN.get_height())

            # Display
            currentMap.update(SCREEN, player1.rect.center, player2.rect.center)
            
            player1.DisplayHealth(SCREEN)
            player2.DisplayHealth(SCREEN)
            player1.DisplayGauge(SCREEN)
            player2.DisplayGauge(SCREEN)

            player1.DisplayEffects(SCREEN)
            player2.DisplayEffects(SCREEN)
            
            SCREEN.blit(player1.image, player1.rect)
            SCREEN.blit(player2.image, player2.rect)


           #pygame.draw.rect(SCREEN, "black", player2.rect)

            if not player1.isNotAttacking:
                player1.DisplayAttack(SCREEN, player1CurrentMove)
                if pygame.time.get_ticks() >= player1.displayCooldown:
                    player1.isNotAttacking = True

            if not player2.isNotAttacking:
                player2.DisplayAttack(SCREEN, player2CurrentMove)
                if pygame.time.get_ticks() >= player2.displayCooldown:
                    player2.isNotAttacking = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentEvent = -1
                    running = False

            pygame.display.update()

        return currentEvent

    def StartSettings():
        currentEvent = 0
        settingsMenu = menus.SettingsMenu(SCREEN)
        #background = Background(SCREEN)

        running = True
        while running:
            CLOCK.tick(60)

            settingsMenu.DrawMenu(SCREEN)
            currentEvent = settingsMenu.RegisterInputs()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentEvent = -1
                    running = False
            if currentEvent:
                running = False

            pygame.display.update()

        return currentEvent

    def StartHelp():
        currentEvent = 0
        displayCharacters = True
        helpMenu = menus.HelpMenu(SCREEN)

        running = True
        while running:
            CLOCK.tick(60)

            helpMenu.DrawMenu(SCREEN, displayCharacters)
            currentEvent = helpMenu.RegisterBackButton()
            displayCharacters = helpMenu.RegisterCharacterDisplayButton(displayCharacters)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentEvent = -1
                    running = False
            if currentEvent == 1:
                currentEvent = 0
                running = False

            pygame.display.update()
        
        return currentEvent

    # List of all the important events:
    # StartMenu = Loads the main menu (Play, settings, help, quit)
    # StartRoundOptions = Loads up the options for the round (characters, maps, etc)
    # StartRound = Starts the round
    # StartSettings = Loads up the settings menu 
    # StartHelp = Loads up the help menu

    EVENT_LIST = [StartMenu, StartRoundOptions, StartRound, StartHelp, StartSettings]

    def MainGame(EVENT_LIST):
        running = True
        currentEvent = 0
        while running:
            match(currentEvent):
                case 0:
                    currentEvent = EVENT_LIST[0]()
                case 1:
                    currentEvent, player1Name, player2Name, selectedMap, player1Input, player2Input = EVENT_LIST[1]()
                case 2:
                    currentEvent = EVENT_LIST[2](player1Name, player2Name, selectedMap, player1Input, player2Input)
                case 3:
                    currentEvent = EVENT_LIST[3]()
                case 4:
                    currentEvent = EVENT_LIST[4]()
                case _:
                    running = False
                    pygame.quit()

    MainGame(EVENT_LIST)
    
if __name__ == "__main__":
    main()
