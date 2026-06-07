import pygame
import playerInputManager

pygame.init()

class MainMenu:
    def __init__(self, SCREEN):
        # Background png, scales it to the size of the screen
        self.background = pygame.image.load("Images\Main menu.png").convert_alpha(SCREEN)
        self.background = pygame.transform.scale(self.background, (SCREEN.get_width(), SCREEN.get_height()))

        # Button measurements so that they are each the same size; proportional to the screen size
        buttonWidth = SCREEN.get_width() / 8
        buttonHeight = SCREEN.get_height() / 10
        screenCenter = (SCREEN.get_width() / 2, SCREEN.get_height() / 2)

        # Play button
        self.play = pygame.image.load("Images\play.png").convert_alpha(SCREEN)
        self.play = pygame.transform.scale(self.play, (buttonWidth, buttonHeight))
        self.playRect = self.play.get_rect()
        self.playRect.center = screenCenter

        # Help button
        self.help = pygame.image.load("Images\help.png").convert_alpha(SCREEN)
        self.help = pygame.transform.scale(self.help, (buttonWidth, buttonHeight))
        self.helpRect = self.help.get_rect()
        self.helpRect.center = (screenCenter[0], screenCenter[1] + self.helpRect.height * 1.1)

        # Settings button
        self.settings = pygame.image.load("Images\settings.png").convert_alpha(SCREEN)
        self.settings = pygame.transform.scale(self.settings, (buttonWidth, buttonHeight))
        self.settingsRect = self.settings.get_rect()
        self.settingsRect.center = (screenCenter[0], screenCenter[1] + self.settingsRect.height * 2.2)

        # Quit button
        self.quit = pygame.image.load("Images\quit.png").convert_alpha(SCREEN)
        self.quit = pygame.transform.scale(self.quit, (buttonWidth, buttonHeight))
        self.quitRect = self.quit.get_rect()
        self.quitRect.center = (screenCenter[0], screenCenter[1] + self.quitRect.height * 3.3)
    def DrawMenu(self, SCREEN):
        SCREEN.blit(self.background, (0,0))
        SCREEN.blit(self.play, self.playRect)
        SCREEN.blit(self.help, self.helpRect)
        SCREEN.blit(self.settings, self.settingsRect)
        SCREEN.blit(self.quit, self.quitRect)
    def RegisterInputs(self):
        buttonPressed = 0

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.playRect.collidepoint(mousePos):
                buttonPressed = 1
            elif self.helpRect.collidepoint(mousePos):
                buttonPressed = 3
            elif self.settingsRect.collidepoint(mousePos):
                buttonPressed = 4
            elif self.quitRect.collidepoint(mousePos):
                buttonPressed = 5

        return buttonPressed

class RoundSettings:
    def __init__(self, SCREEN):

        # Left half of the screen
        self.leftHalfScreen = pygame.Rect((0,0), (SCREEN.get_width() / 2, SCREEN.get_height()))
        self.rightHalfScreen = pygame.Rect((SCREEN.get_width() / 2, 0), (SCREEN.get_width() / 2, SCREEN.get_height()))

        # Back button
        self.back = pygame.image.load("Images/back.png").convert_alpha(SCREEN)
        self.back = pygame.transform.scale(self.back, (SCREEN.get_width() / 8,SCREEN.get_height() / 10))
        self.backRect = self.back.get_rect()
        self.backRect.topleft = (0,0)

        # Start Buttons (width and height)
        self.startButtonWidth = SCREEN.get_width() / 7
        self.startButtonHeight = SCREEN.get_height() / 5

        # Start button (left)
        self.startLeft = pygame.image.load("Images/start.png").convert_alpha(SCREEN)
        self.startLeft = pygame.transform.scale(self.startLeft, (self.startButtonWidth, self.startButtonHeight))
        self.startLeftRect = self.startLeft.get_rect()
        self.startLeftRect.topleft = (0, SCREEN.get_height() * 4/5)

        # Start button (right)
        self.startRight = pygame.image.load("Images/start.png").convert_alpha(SCREEN)
        self.startRight = pygame.transform.scale(self.startRight, (self.startButtonWidth, self.startButtonHeight))
        self.startRightRect = self.startRight.get_rect()
        self.startRightRect.topleft = (SCREEN.get_width() * 6/7, SCREEN.get_height() * 4/5)

        # Player selection buttons
        # Sizes:
        playerSelectionButtonWidth = SCREEN.get_width() / 7
        playerSelectionButtonHeight = SCREEN.get_height() / 10

        # Text font
        self.textFont = pygame.font.SysFont("Arial", 50)

        # Button that shows the left side is player 1
        self.player1Text = pygame.image.load("Images/player_1_text.png").convert_alpha(SCREEN)
        self.player1Text = pygame.transform.scale(self.player1Text, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.player1TextRect = self.player1Text.get_rect()
        self.player1TextRect.topright = (SCREEN.get_width() / 2, 0)

        # Button that shows the left side is player 2
        self.player2Text = pygame.image.load("Images/player_2_text.png").convert_alpha(SCREEN)
        self.player2Text = pygame.transform.scale(self.player2Text, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.player2TextRect = self.player2Text.get_rect()
        self.player2TextRect.topleft = (SCREEN.get_width() / 2, 0)

        # For switching to keyboard
        self.useKeyboard = pygame.image.load("Images/use_keyboard.png").convert_alpha(SCREEN)
        self.useKeyboard = pygame.transform.scale(self.useKeyboard, (playerSelectionButtonWidth, playerSelectionButtonHeight))

        self.useKeyboardPlayer1Rect = self.useKeyboard.get_rect()
        self.useKeyboardPlayer1Rect.topright = self.player1TextRect.bottomright

        self.useKeyboardPlayer2Rect = self.useKeyboard.get_rect()
        self.useKeyboardPlayer2Rect.topleft = self.player2TextRect.bottomleft
        
        # For switching to controller
        self.useController = pygame.image.load("Images/use_controller.png").convert_alpha(SCREEN)
        self.useController = pygame.transform.scale(self.useController, (playerSelectionButtonWidth, playerSelectionButtonHeight))

        self.useControllerPlayer1Rect = self.useController.get_rect()
        self.useControllerPlayer1Rect.topright = self.useKeyboardPlayer1Rect.bottomright

        self.useControllerPlayer2Rect = self.useController.get_rect()
        self.useControllerPlayer2Rect.topleft = self.useKeyboardPlayer2Rect.bottomleft

        # Keyboard / Controller text rect
        # Player 1
        self.currentInputPlayer1Rect = pygame.Rect(0,0, playerSelectionButtonWidth, playerSelectionButtonHeight)
        self.currentInputPlayer1Rect.topright = self.player1TextRect.topleft

        # Player 2
        self.currentInputPlayer2Rect = pygame.Rect(0,0, playerSelectionButtonWidth, playerSelectionButtonHeight)
        self.currentInputPlayer2Rect.topleft = self.player2TextRect.topright

        # Player 1 selection buttons
        # Etai 1 button
        self.etai1 = pygame.image.load("Images/etai_1_text.png").convert_alpha(SCREEN)
        self.etai1 = pygame.transform.scale(self.etai1, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.etai1Rect = self.etai1.get_rect()
        self.etai1Rect.center = (SCREEN.get_width() * 1/12, SCREEN.get_height() * 4/11)

        # Tane 1 button
        self.tane1 = pygame.image.load("Images/tane_1_text.png").convert_alpha(SCREEN)
        self.tane1 = pygame.transform.scale(self.tane1, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.tane1Rect = self.tane1.get_rect()
        self.tane1Rect.center = (SCREEN.get_width() * 3/12, SCREEN.get_height() * 6/11)
        
        # Neor 1 button
        self.neor1 = pygame.image.load("Images/neor_1_text.png").convert_alpha(SCREEN)
        self.neor1 = pygame.transform.scale(self.neor1, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.neor1Rect = self.neor1.get_rect()
        self.neor1Rect.center = (SCREEN.get_width() * 5/12, SCREEN.get_height() * 8/11)

        # Player 2 selection buttons
        # Etai 2 button
        self.etai2 = pygame.image.load("Images/etai_2_text.png").convert_alpha(SCREEN)
        self.etai2 = pygame.transform.scale(self.etai2, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.etai2Rect = self.etai2.get_rect()
        self.etai2Rect.center = (SCREEN.get_width() * 11/12, SCREEN.get_height() * 4/11)

        # Tane 2 button
        self.tane2 = pygame.image.load("Images/tane_1_text.png").convert_alpha(SCREEN)
        self.tane2 = pygame.transform.scale(self.tane2, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.tane2Rect = self.tane2.get_rect()
        self.tane2Rect.center = (SCREEN.get_width() * 9/12, SCREEN.get_height() * 6/11)

        # Neor 2 button
        self.neor2 = pygame.image.load("Images/neor_2_text.png").convert_alpha(SCREEN)
        self.neor2 = pygame.transform.scale(self.neor2, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.neor2Rect = self.neor2.get_rect()
        self.neor2Rect.center = (SCREEN.get_width() * 7/12, SCREEN.get_height() * 8/11)

        # Background Buttons
        # Colosseum Button
        self.colosseumButton = pygame.image.load("Images/colosseum_button.png").convert_alpha(SCREEN)
        self.colosseumButton = pygame.transform.scale(self.colosseumButton, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.colosseumButtonRect = self.colosseumButton.get_rect()
        self.colosseumButtonRect.center = (SCREEN.get_width() * 2/7, SCREEN.get_height() * 9/10)

        # Tundra Button
        self.tundraButton = pygame.image.load("Images/tundra_button.png").convert_alpha(SCREEN)
        self.tundraButton = pygame.transform.scale(self.tundraButton, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.tundraButtonRect = self.tundraButton.get_rect()
        self.tundraButtonRect.center = (SCREEN.get_width() * 3/7, SCREEN.get_height() * 9/10)

        # Clockwork Button
        self.clockworkButton = pygame.image.load("Images/clockwork_button.png").convert_alpha(SCREEN)
        self.clockworkButton = pygame.transform.scale(self.clockworkButton, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.clockworkButtonRect = self.clockworkButton.get_rect()
        self.clockworkButtonRect.center = (SCREEN.get_width() * 4/7, SCREEN.get_height() * 9/10)

        # Warter Button
        self.warterButton = pygame.image.load("Images/warter_button.png").convert_alpha(SCREEN)
        self.warterButton = pygame.transform.scale(self.warterButton, (playerSelectionButtonWidth, playerSelectionButtonHeight))
        self.warterButtonRect = self.warterButton.get_rect()
        self.warterButtonRect.center = (SCREEN.get_width() * 5/7, SCREEN.get_height() * 9/10)
    def BlitRoundSettings(self, SCREEN, currentPlayer1Input, currentPlayer2Input):
        # Start button (left)
        SCREEN.blit(self.startLeft, self.startLeftRect)
        # Start button (right)
        SCREEN.blit(self.startRight, self.startRightRect)

        # Top left and top right lines (meeting at the middle)
        pygame.draw.line(SCREEN, "white", (0,SCREEN.get_height() / 6), (SCREEN.get_width() / 2, SCREEN.get_height() / 2))
        pygame.draw.line(SCREEN, "white", (SCREEN.get_width() / 2, SCREEN.get_height() / 2), (SCREEN.get_width(), SCREEN.get_height() / 6))

        # Middle line (going down the middle)
        pygame.draw.line(SCREEN, "white", (SCREEN.get_width() / 2, 0), (SCREEN.get_width() / 2, SCREEN.get_height() * 4/5))

        # Horizontal bottom line
        pygame.draw.line(SCREEN, "white", (0, SCREEN.get_height() * 4/5), (SCREEN.get_width(), SCREEN.get_height() * 4/5))

        # TEST - HORIZONTAL
        #pygame.draw.line(SCREEN, "white", (0, SCREEN.get_height() * 3/11), (SCREEN.get_width(), SCREEN.get_height() * 3/11))
        #pygame.draw.line(SCREEN, "white", (0, SCREEN.get_height() * 5/11), (SCREEN.get_width(), SCREEN.get_height() * 5/11))
        #pygame.draw.line(SCREEN, "white", (0, SCREEN.get_height() * 7/11), (SCREEN.get_width(), SCREEN.get_height() * 7/11))

        # TEST - VERTICAL
        #pygame.draw.line(SCREEN, "white", (SCREEN.get_width() * 1/7, 0), (SCREEN.get_width() * 1/7, SCREEN.get_height()))
        #pygame.draw.line(SCREEN, "white", (SCREEN.get_width() * 2/7, 0), (SCREEN.get_width() * 2/7, SCREEN.get_height()))
        #pygame.draw.line(SCREEN, "white", (SCREEN.get_width() * 3/7, 0), (SCREEN.get_width() * 3/7, SCREEN.get_height()))
        # Lines next to left and right start
        pygame.draw.line(SCREEN, "white", (SCREEN.get_width() * 1/7, SCREEN.get_height() * 4/5), (SCREEN.get_width() * 1/7, SCREEN.get_height()))
        pygame.draw.line(SCREEN, "white", (SCREEN.get_width() * 6/7, SCREEN.get_height() * 4/5), (SCREEN.get_width() * 6/7, SCREEN.get_height()))

        # Back button
        SCREEN.blit(self.back, self.backRect)

        # Player 1 buttons
        SCREEN.blit(self.etai1, self.etai1Rect)
        SCREEN.blit(self.tane1, self.tane1Rect)
        SCREEN.blit(self.neor1, self.neor1Rect)
        SCREEN.blit(self.player1Text, self.player1TextRect)
        SCREEN.blit(self.useKeyboard, self.useKeyboardPlayer1Rect)
        SCREEN.blit(self.useController, self.useControllerPlayer1Rect)
        SCREEN.blit(self.textFont.render(currentPlayer1Input, True, "white", "black"), self.currentInputPlayer1Rect)

        # Player 2 buttons
        SCREEN.blit(self.etai2, self.etai2Rect)
        SCREEN.blit(self.tane2, self.tane2Rect)
        SCREEN.blit(self.neor2, self.neor2Rect)
        SCREEN.blit(self.player2Text, self.player2TextRect)
        SCREEN.blit(self.useKeyboard, self.useKeyboardPlayer2Rect)
        SCREEN.blit(self.useController, self.useControllerPlayer2Rect)
        SCREEN.blit(self.textFont.render(currentPlayer2Input, True, "white", "black"), self.currentInputPlayer2Rect)

        # Map buttons
        SCREEN.blit(self.colosseumButton, self.colosseumButtonRect)
        SCREEN.blit(self.tundraButton, self.tundraButtonRect)
        SCREEN.blit(self.clockworkButton, self.clockworkButtonRect)
        SCREEN.blit(self.warterButton, self.warterButtonRect)
    def ActivateReadyButton(self, isPlayer1):
        if isPlayer1:
            self.startLeft = pygame.image.load("Images/start_activated.png").convert_alpha()
            self.startLeft = pygame.transform.scale(self.startLeft, (self.startButtonWidth, self.startButtonHeight))
        else:
            self.startRight = pygame.image.load("Images/start_activated.png").convert_alpha()
            self.startRight = pygame.transform.scale(self.startRight, (self.startButtonWidth, self.startButtonHeight))
    def RegisterInputs(self):
        buttonPressed = 0

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.backRect.collidepoint(mousePos):
                buttonPressed = 1
            elif self.etai1Rect.collidepoint(mousePos):
                buttonPressed = 2
            elif self.tane1Rect.collidepoint(mousePos):
                buttonPressed = 3
            elif self.neor1Rect.collidepoint(mousePos):
                buttonPressed = 4
            elif self.etai2Rect.collidepoint(mousePos):
                buttonPressed = 5
            elif self.tane2Rect.collidepoint(mousePos):
                buttonPressed = 6
            elif self.neor2Rect.collidepoint(mousePos):
                buttonPressed = 7
            elif self.startLeftRect.collidepoint(mousePos):
                buttonPressed = 8
            elif self.startRightRect.collidepoint(mousePos):
                buttonPressed = 9
            elif self.colosseumButtonRect.collidepoint(mousePos):
                buttonPressed = 10
            elif self.tundraButtonRect.collidepoint(mousePos):
                buttonPressed = 11
            elif self.clockworkButtonRect.collidepoint(mousePos):
                buttonPressed = 12
            elif self.warterButtonRect.collidepoint(mousePos):
                buttonPressed = 13
            elif self.useKeyboardPlayer1Rect.collidepoint(mousePos):
                buttonPressed = 14
            elif self.useControllerPlayer1Rect.collidepoint(mousePos):
                buttonPressed = 15
            elif self.useKeyboardPlayer2Rect.collidepoint(mousePos):
                buttonPressed = 16
            elif self.useControllerPlayer2Rect.collidepoint(mousePos):
                buttonPressed = 17
        return buttonPressed
    def BlitEffect(self, SCREEN, player1Name, player2Name):
        leftHalfColor = (0,0,0)
        rightHalfColor = (0,0,0)

        match(player1Name):
            case "Etai":
                leftHalfColor = (242, 0 , 0)
            case "Tane":
                leftHalfColor = (128, 128, 128)
            case "Neor":
                leftHalfColor = (49, 143, 33)
        match(player2Name):
            case "Etai":
                rightHalfColor = (255, 97, 97)
            case "Tane":
                rightHalfColor = (191, 191, 191)
            case "Neor":
                rightHalfColor = (92, 212, 72)

        SCREEN.fill(leftHalfColor, self.leftHalfScreen)
        SCREEN.fill(rightHalfColor, self.rightHalfScreen)

class SettingsMenu:
    def __init__(self, SCREEN):
        # Button measurements (for the majority of the buttons)
        self.buttonWidth = SCREEN.get_width() / 7
        self.buttonHeight = SCREEN.get_height() / 11
        
        # Back button
        self.back = pygame.image.load("Images/back.png").convert_alpha(SCREEN)
        self.back = pygame.transform.scale(self.back, (SCREEN.get_width() / 8,SCREEN.get_height() / 10))
        self.backRect = self.back.get_rect()
        self.backRect.topleft = (0,0)

        # Rebind text
        self.rebind = pygame.image.load("Images/rebind.png").convert_alpha(SCREEN)
        self.rebind = pygame.transform.scale(self.rebind, (self.buttonWidth, self.buttonHeight))
        self.rebindRect = self.rebind.get_rect()
        self.rebindRect.center = (SCREEN.get_width() * 3/4, SCREEN.get_height() / 6)
        # Rebind button (next to each text)
        self.rebindButton = pygame.image.load("Images/rebind_text.png").convert_alpha(SCREEN)
        self.rebindButton = pygame.transform.scale(self.rebind, (SCREEN.get_width() / 6, SCREEN.get_height() / 10))

        # Volume text
        self.volume = pygame.image.load("Images/volume.png").convert_alpha(SCREEN)
        self.volume = pygame.transform.scale(self.volume, (self.buttonWidth, self.buttonHeight))
        self.volumeRect = self.volume.get_rect()
        self.volumeRect.center = (SCREEN.get_width() / 4, SCREEN.get_height() / 6)

        # Player 1 text
        self.player1Text = pygame.image.load("Images/player_1_text.png").convert_alpha(SCREEN)
        self.player1Text = pygame.transform.scale(self.player1Text, (self.buttonWidth, self.buttonHeight))
        self.player1TextRect = self.player1Text.get_rect()
        self.player1TextRect.center = (SCREEN.get_width() * 5/8, SCREEN.get_height() / 3.5)

        # Player 2 text
        self.player2Text = pygame.image.load("Images/player_2_text.png").convert_alpha(SCREEN)
        self.player2Text = pygame.transform.scale(self.player2Text, (self.buttonWidth, self.buttonHeight))
        self.player2TextRect = self.player2Text.get_rect()
        self.player2TextRect.center = (SCREEN.get_width() * 7/8, SCREEN.get_height() / 3.5)

        # Everything below player text:
        self.rebindTextFont = pygame.font.SysFont("Arial", 50)

        # Player 1 text rect
        self.jumpKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 6/16,0,0)
        self.leftKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 7/16,0,0)
        self.rightKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 8/16,0,0)
        self.specialAttackKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 9/16,0,0)
        self.ultimateAttackKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 10/16,0,0)
        self.blockKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 11/16,0,0)
        self.vanishKeyTextRect1 = pygame.Rect(SCREEN.get_width() * 9/16, SCREEN.get_height() * 12/16,0,0)

        # Plater 2 text rect
        self.jumpKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 6/16,0,0)
        self.leftKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 7/16,0,0)
        self.rightKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 8/16,0,0)
        self.specialAttackKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 9/16,0,0)
        self.ultimateAttackKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 10/16,0,0)
        self.blockKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 11/16,0,0)
        self.vanishKeyTextRect2 = pygame.Rect(SCREEN.get_width() * 13/16, SCREEN.get_height() * 12/16,0,0)

        # Player 1 inputs (rebind)
        self.player1Inputs = playerInputManager.PlayerKeyboardInput.GetCurrentInputs(True)
        # Player 2 inputs (rebind)
        self.player2Inputs = playerInputManager.PlayerKeyboardInput.GetCurrentInputs(False)

    def DrawMenu(self, SCREEN):
        SCREEN.fill("black")
        
        # Back button
        SCREEN.blit(self.back, self.backRect)

        # Rebind button (Visual)
        SCREEN.blit(self.rebind, self.rebindRect)

        # Volume button (Visual)
        SCREEN.blit(self.volume, self.volumeRect)

        # Player 1 Text button (Visual)
        SCREEN.blit(self.player1Text, self.player1TextRect)

        # Player 1 texts (below button)
        SCREEN.blit(self.rebindTextFont.render("Jump:"+ chr(int(self.player1Inputs["JUMP"])), True, "white", "black"), self.jumpKeyTextRect1)
        SCREEN.blit(self.rebindTextFont.render("Move Left:"+ chr(int(self.player1Inputs["MOVE_LEFT"])), True, "white", "black"), self.leftKeyTextRect1)
        SCREEN.blit(self.rebindTextFont.render("Move Right:"+ chr(int(self.player1Inputs["MOVE_RIGHT"])), True, "white", "black"), self.rightKeyTextRect1)
        SCREEN.blit(self.rebindTextFont.render("Special Attack:"+ chr(int(self.player1Inputs["SPECIAL_ATTACK"])), True, "white", "black"), self.specialAttackKeyTextRect1)
        SCREEN.blit(self.rebindTextFont.render("Ultimate Attack:"+ chr(int(self.player1Inputs["ULTIMATE_ATTACK"])), True, "white", "black"), self.ultimateAttackKeyTextRect1)
        SCREEN.blit(self.rebindTextFont.render("Block:"+ chr(int(self.player1Inputs["BLOCK"])), True, "white", "black"), self.blockKeyTextRect1)
        SCREEN.blit(self.rebindTextFont.render("Vanish:"+ chr(int(self.player1Inputs["VANISH"])), True, "white", "black"), self.vanishKeyTextRect1)
        
        # Player 2 texts (below button)
        SCREEN.blit(self.rebindTextFont.render("Jump:"+ chr(int(self.player2Inputs["JUMP"])), True, "white", "black"), self.jumpKeyTextRect2)
        SCREEN.blit(self.rebindTextFont.render("Move Left:"+ chr(int(self.player2Inputs["MOVE_LEFT"])), True, "white", "black"), self.leftKeyTextRect2)
        SCREEN.blit(self.rebindTextFont.render("Move Right:"+ chr(int(self.player2Inputs["MOVE_RIGHT"])), True, "white", "black"), self.rightKeyTextRect2)
        SCREEN.blit(self.rebindTextFont.render("Special Attack:"+ chr(int(self.player2Inputs["SPECIAL_ATTACK"])), True, "white", "black"), self.specialAttackKeyTextRect2)
        SCREEN.blit(self.rebindTextFont.render("Ultimate Attack:"+ chr(int(self.player2Inputs["ULTIMATE_ATTACK"])), True, "white", "black"), self.ultimateAttackKeyTextRect2)
        SCREEN.blit(self.rebindTextFont.render("Block:"+ chr(int(self.player2Inputs["BLOCK"])), True, "white", "black"), self.blockKeyTextRect2)
        SCREEN.blit(self.rebindTextFont.render("Vanish:"+ chr(int(self.player2Inputs["VANISH"])), True, "white", "black"), self.vanishKeyTextRect2)

        # Player 2 Text button (Visual)
        SCREEN.blit(self.player2Text, self.player2TextRect)

    def RegisterInputs(self):
        buttonPressed = 0

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.backRect.collidepoint(mousePos):
                buttonPressed = 1
        return buttonPressed

class HelpMenu:
    def __init__(self, SCREEN):
        self.buttonWidth = SCREEN.get_width() / 7
        self.buttonHeight = SCREEN.get_height() / 11

        self.characterDescriptionWidth = SCREEN.get_width() / 3
        self.descriptionHeight = SCREEN.get_height() *7/ 10

        self.basicControlsDescriptionWidth = SCREEN.get_width() / 4

        # Back button
        self.back = pygame.image.load("Images/back.png").convert_alpha(SCREEN)
        self.back = pygame.transform.scale(self.back, (SCREEN.get_width() / 8,SCREEN.get_height() / 10))
        self.backRect = self.back.get_rect()
        self.backRect.topleft = (0,0)

        # Characters buttons
        self.characters = pygame.image.load("Images/characters_button.png").convert_alpha(SCREEN)
        self.characters = pygame.transform.scale(self.characters, (self.buttonWidth, self.buttonHeight))
        self.charactersRect = self.characters.get_rect()
        self.charactersRect.center = (SCREEN.get_width() * 2/5, SCREEN.get_height() / 8)
        # Etai button (display only)
        self.etaiButton = pygame.image.load("Images/etai_1_text.png").convert_alpha(SCREEN)
        self.etaiButton = pygame.transform.scale(self.etaiButton, (self.buttonWidth, self.buttonHeight))
        self.etaiButtonRect = self.etaiButton.get_rect()
        self.etaiButtonRect.center = (SCREEN.get_width() * 1/6, SCREEN.get_height() / 4)

        self.etaiDescription = pygame.image.load("Images/etai_description_text.png").convert_alpha(SCREEN)
        self.etaiDescription = pygame.transform.scale(self.etaiDescription, (self.characterDescriptionWidth, self.descriptionHeight))
        self.etaiDescriptionRect = self.etaiDescription.get_rect()
        self.etaiDescriptionRect.bottomleft = (0, SCREEN.get_height())
        # Tane button (display only)
        self.taneButton = pygame.image.load("Images/tane_1_text.png").convert_alpha(SCREEN)
        self.taneButton = pygame.transform.scale(self.taneButton, (self.buttonWidth, self.buttonHeight))
        self.taneButtonRect = self.taneButton.get_rect()
        self.taneButtonRect.center = (SCREEN.get_width() / 2, SCREEN.get_height() / 4)

        self.taneDescription = pygame.image.load("Images/tane_description_text.png").convert_alpha(SCREEN)
        self.taneDescription = pygame.transform.scale(self.taneDescription, (self.characterDescriptionWidth, self.descriptionHeight))
        self.taneDescriptionRect = self.taneDescription.get_rect()
        self.taneDescriptionRect.bottomleft = (SCREEN.get_width() / 3, SCREEN.get_height())
        # Neor button (display only)
        self.neorButton = pygame.image.load("Images/neor_1_text.png").convert_alpha(SCREEN)
        self.neorButton = pygame.transform.scale(self.neorButton, (self.buttonWidth, self.buttonHeight))
        self.neorButtonRect = self.neorButton.get_rect()
        self.neorButtonRect.center = (SCREEN.get_width() * 5/6, SCREEN.get_height() / 4)

        self.neorDescription = pygame.image.load("Images/neor_description_text.png").convert_alpha(SCREEN)
        self.neorDescription = pygame.transform.scale(self.neorDescription, (self.characterDescriptionWidth, self.descriptionHeight))
        self.neorDescriptionRect = self.neorDescription.get_rect()
        self.neorDescriptionRect.bottomleft = (SCREEN.get_width() * 2/3, SCREEN.get_height())
        # Basic controls buttons
        self.basicControls = pygame.image.load("Images/basic_controls.png").convert_alpha(SCREEN)
        self.basicControls = pygame.transform.scale(self.basicControls, (self.buttonWidth, self.buttonHeight))
        self.basicControlsRect = self.basicControls.get_rect()
        self.basicControlsRect.center = (SCREEN.get_width() * 4/5, SCREEN.get_height() / 8)
        # Combos button (display only)
        self.combosButton = pygame.image.load("Images/combos_text.png").convert_alpha(SCREEN)
        self.combosButton = pygame.transform.scale(self.combosButton, (self.buttonWidth, self.buttonHeight))
        self.combosButtonRect = self.combosButton.get_rect()
        self.combosButtonRect.center = (SCREEN.get_width() / 8, SCREEN.get_height() / 4)

        self.combosDescription = pygame.image.load("Images/combos_description_text.png").convert_alpha(SCREEN)
        self.combosDescription = pygame.transform.scale(self.combosDescription, (self.basicControlsDescriptionWidth, self.descriptionHeight))
        self.combosDescriptionRect = self.combosDescription.get_rect()
        self.combosDescriptionRect.bottomleft = (0, SCREEN.get_height())
        
        # Special Attacks button (display only)
        self.specialAttacksButton = pygame.image.load("Images/special_attack_text.png").convert_alpha(SCREEN)
        self.specialAttacksButton = pygame.transform.scale(self.specialAttacksButton, (self.buttonWidth, self.buttonHeight))
        self.specialAttacksButtonRect = self.specialAttacksButton.get_rect()
        self.specialAttacksButtonRect.center = (SCREEN.get_width() * 3/8, SCREEN.get_height() / 4)

        self.specialAttacksDescription = pygame.image.load("Images/special_attacks_description_text.png").convert_alpha(SCREEN)
        self.specialAttacksDescription = pygame.transform.scale(self.specialAttacksDescription, (self.basicControlsDescriptionWidth, self.descriptionHeight))
        self.specialAttacksDescriptionRect = self.specialAttacksDescription.get_rect()
        self.specialAttacksDescriptionRect.bottomleft = (SCREEN.get_width() / 4, SCREEN.get_height())
        # Ultimate Attacks button (display only)
        self.ultimateAttacksButton = pygame.image.load("Images/ultimate_attack_text.png").convert_alpha(SCREEN)
        self.ultimateAttacksButton = pygame.transform.scale(self.ultimateAttacksButton, (self.buttonWidth, self.buttonHeight))
        self.ultimateAttacksButtonRect = self.ultimateAttacksButton.get_rect()
        self.ultimateAttacksButtonRect.center = (SCREEN.get_width() * 5/8, SCREEN.get_height() / 4)

        self.ultimateAttacksDescription = pygame.image.load("Images/ultimate_attacks_description_text.png").convert_alpha(SCREEN)
        self.ultimateAttacksDescription = pygame.transform.scale(self.ultimateAttacksDescription, (self.basicControlsDescriptionWidth, self.descriptionHeight))
        self.ultimateAttacksDescriptionRect = self.ultimateAttacksDescription.get_rect()
        self.ultimateAttacksDescriptionRect.bottomleft = (SCREEN.get_width() / 2, SCREEN.get_height())
        # Blocking button (display only)
        self.blockingButton = pygame.image.load("Images/blocking_text.png").convert_alpha(SCREEN)
        self.blockingButton = pygame.transform.scale(self.blockingButton, (self.buttonWidth, self.buttonHeight))
        self.blockingButtonRect = self.blockingButton.get_rect()
        self.blockingButtonRect.center = (SCREEN.get_width() * 7/8, SCREEN.get_height() / 4)

        self.blockingDescription = pygame.image.load("Images/blocking_description_text.png").convert_alpha(SCREEN)
        self.blockingDescription = pygame.transform.scale(self.blockingDescription, (self.basicControlsDescriptionWidth, self.descriptionHeight))
        self.blockingDescriptionRect = self.blockingDescription.get_rect()
        self.blockingDescriptionRect.bottomleft = (SCREEN.get_width() * 3/4, SCREEN.get_height())

    def DrawMenu(self, SCREEN, displayCharacters):
        SCREEN.fill("black")
        
        # Buttons
        SCREEN.blit(self.back, self.backRect)
        SCREEN.blit(self.characters, self.charactersRect)
        SCREEN.blit(self.basicControls, self.basicControlsRect)

        if displayCharacters:
            SCREEN.blit(self.etaiButton, self.etaiButtonRect)
            SCREEN.blit(self.etaiDescription, self.etaiDescriptionRect)
            
            SCREEN.blit(self.taneButton, self.taneButtonRect)
            SCREEN.blit(self.taneDescription, self.taneDescriptionRect)
            
            SCREEN.blit(self.neorButton, self.neorButtonRect)
            SCREEN.blit(self.neorDescription, self.neorDescriptionRect)
        else:
            SCREEN.blit(self.combosButton, self.combosButtonRect)
            SCREEN.blit(self.combosDescription, self.combosDescriptionRect)

            SCREEN.blit(self.specialAttacksButton, self.specialAttacksButtonRect)
            SCREEN.blit(self.specialAttacksDescription, self.specialAttacksDescriptionRect)

            SCREEN.blit(self.ultimateAttacksButton, self.ultimateAttacksButtonRect)
            SCREEN.blit(self.ultimateAttacksDescription, self.ultimateAttacksDescriptionRect)

            SCREEN.blit(self.blockingButton, self.blockingButtonRect)
            SCREEN.blit(self.blockingDescription, self.blockingDescriptionRect)

    def RegisterBackButton(self):
        buttonPressed = 0

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.backRect.collidepoint(mousePos):
                buttonPressed = 1
        return buttonPressed
    def RegisterCharacterDisplayButton(self, displayCharacters):
        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.charactersRect.collidepoint(mousePos):
                displayCharacters = True
            elif self.basicControlsRect.collidepoint(mousePos):
                displayCharacters = False
        return displayCharacters
    
