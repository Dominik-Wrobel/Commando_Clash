import pygame
import playerInputManager

pygame.init()
pygame.joystick.init()

class Character(pygame.sprite.Sprite):
    def __init__(self, SCREEN, pIsPlayer1, pInputType):
        pygame.sprite.Sprite.__init__(self)

        # Basics
        self.characterWidth = SCREEN.get_width() / 12
        self.characterHeight = SCREEN.get_height() / 10
        self.rect = pygame.Rect(0,0,0,0)
        self.name = ""
        self.speed = 200
        self.image = None
        self.imagePath = ""

        # Health manager + rects
        self.maxHealth = 1000
        self.health = 1000

        if pIsPlayer1:
            healthRectPos = (SCREEN.get_width() / 20, SCREEN.get_height() / 18)
        else:
            healthRectPos = (SCREEN.get_width() * (11 / 20), SCREEN.get_height() / 18)
        self.maxHealthRect = pygame.Rect(healthRectPos[0], healthRectPos[1], SCREEN.get_width() / 2.3, SCREEN.get_height() / 17)
        self.healthRect = pygame.Rect(healthRectPos[0], healthRectPos[1], SCREEN.get_width() / 2.3, SCREEN.get_height() / 17)

        # Gauge manager + rects
        self.maxGaugeAmount = 300
        self.currentGaugeAmount = 100

        gaugeRectPos = (healthRectPos[0], SCREEN.get_height() * 19/20)

        self.maxGaugeRect = pygame.Rect(gaugeRectPos[0], gaugeRectPos[1], SCREEN.get_width() / 5, SCREEN.get_height() / 18)
        self.gaugeRect = pygame.Rect(gaugeRectPos[0], gaugeRectPos[1], 0, SCREEN.get_height() / 18)
        self.gaugeRect.width = self.maxGaugeRect.width * (self.currentGaugeAmount / self.maxGaugeAmount)

        if not pIsPlayer1:
            self.gaugeRect.right = self.maxGaugeRect.right


        # Whether the player is using keyboard or player is using a controller
        self.usingKeyboard = True
        self.joystick = None

        # Gets the current keyboard inputs
        self.currentInputs = None
        if pInputType[0] == "Keyboard":
            self.currentInputs = playerInputManager.PlayerKeyboardInput.GetCurrentInputs(pIsPlayer1)
            self.usingKeyboard = True
        else:
            self.currentInputs = playerInputManager.PlayerControllerInput.GetCurrentInputs()
            self.usingKeyboard = False
            self.joystick = pygame.joystick.Joystick(pInputType[1] - 1)

        # Setting up correct model
        self.isPlayer1 = pIsPlayer1

        # For flipping the player in the correct direction (based on where they're moving)
        # Is true if the player is facing right
        self.isFlipped = pIsPlayer1

        # For the gravity section (i.e. jumping)
        self.yvelocity = 0
        self.gravity = False

        #### For Attacks / Moves ####
        # For when the player is hit
        self.stunned = False
        self.stunTime = 0
        self.currentRotation = 0
        # Used to register whether the player is attacking or not
        self.isNotAttacking = True
        # Used to flip the attack based on the direction the player is facing
        self.isAttackFlipped = pIsPlayer1
        self.displayCooldown = 0


        # Dictionary of attacks and whether they are flipped or not
        self.flippedAttacks = {"REGULAR_ATTACK":pIsPlayer1, "HEAVY_ATTACK":pIsPlayer1, "SPECIAL_ATTACK":pIsPlayer1, "ULTIMATE_ATTACK":pIsPlayer1}
        # Dictionary of attacks and their cooldowns
        self.cooldownAttacks = {"REGULAR_ATTACK":0, "HEAVY_ATTACK":0, "BLOCK":0, "SPECIAL_ATTACK":0, "ULTIMATE_ATTACK":0, "VANISH":0}

        # Regular attack setup
        self.regularAttack = pygame.image.load("Images/players/regular_attack.png").convert_alpha(SCREEN)
        self.regularAttack = pygame.transform.scale(self.regularAttack, (self.characterWidth / 2, self.characterHeight / 3))
        if pIsPlayer1:
            self.regularAttack = pygame.transform.flip(self.regularAttack, True, False)
        self.regularAttackRect = self.regularAttack.get_rect()
        self.regularAttackDamage = 10
        # Heavy attack setup
        self.heavyAttack = pygame.image.load("Images/players/heavy_attack.png").convert_alpha(SCREEN)
        self.heavyAttack = pygame.transform.scale(self.heavyAttack, (self.characterWidth / 1.5, self.characterHeight / 1.7))
        if pIsPlayer1:
            self.heavyAttack = pygame.transform.flip(self.heavyAttack, True, False)
        self.heavyAttackRect = self.heavyAttack.get_rect()
        self.heavyAttackDamage = 20
        # Blocking setup
        self.isBlocking = False

    def CheckGravity(self, GROUND_BOUNDARY):
        # If the players bottom rect is taller than slightly above the ground boundary, the player
        # falls (I.e. for when the player is flung into the air, they're supposed to fall 
        if self.rect.bottom < GROUND_BOUNDARY - 1:
            self.gravity = True
        # If the players bottom rect is below the ground boundary, the players' hitbox is set to be on
        # the ground, prevents the player from clipping into the ground
        elif self.rect.bottom > GROUND_BOUNDARY:
            self.rect.bottom = GROUND_BOUNDARY
            self.gravity = False
            self.yvelocity = 0

    # This functions applies vertical velocity to the player and sets gravity to true
    def Jump(self):
        # The yvelocity is set to this value as it will remain constant with the SCREEN size.
        # I.e. The jump will always be the same height, even on different sized monitors
        self.yvelocity = -self.characterHeight / 9
        self.gravity = True

    def UseGravity(self, dt):
        # Same with the previous function, the yvelocity will decrease the same amount even with
        # the screen size changing. dt helps keep the jumping consistent with the frame rate.
        self.yvelocity += ((self.characterHeight / 7) * dt)
        self.rect.y += self.yvelocity

    # GROUND_BOUNDARY is at (SCREEN.get_height() * 9 / 11) by default
    # Update function for the player, updates gravity and collision
    def update(self, SCREEN, dt):
        # If self.gravity is set to true, gravity is applied
        if self.gravity == True:
            self.UseGravity(dt)
        # Checks gravity
        self.CheckGravity(SCREEN.get_height() * 10/11)
        self.CollisionDetection(SCREEN.get_width())

    # Makes sure that players stay within the boundaries of the game
    def CollisionDetection(self, SCREEN_WIDTH):
        # Makes sure that the player's left side doesn't go past the left side of the screen
        if self.rect.left < 0:
            self.rect.left = 0
        # Makes sure that the player's right side doesn't go past the boundary on the right
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def DisplayEffects(self, SCREEN):
        pass

    def ChangeCurrentInputType(self, changeToKeyboard, numControllers):
        if changeToKeyboard:
            self.usingKeyboard = True
            self.joystick = None
            self.currentInputs = playerInputManager.PlayerKeyboardInput.GetCurrentInputs(self.isPlayer1)
        else:
            self.usingKeyboard = False
            self.joystick = None
            self.currentInputs = playerInputManager.PlayerControllerInput.GetCurrentInputs(self.isPlayer1)

    def MovePlayer(self, keyPressed, dt):
        if self.usingKeyboard:
            self.MovePlayerKeyboard(keyPressed, dt)
        else:
            self.MovePlayerController(dt)

    # Keyboard Controls
    def MovePlayerKeyboard(self, keys, dt):
        # If the move right key is pressed, then move right
        if keys[int(self.currentInputs["MOVE_RIGHT"])]:
            self.rect.x += self.speed *dt
            # If the player is not flipped (facing left), then flip the player
            if not self.isFlipped:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isFlipped = True
        # If the move left key is pressed, then move left
        if keys[int(self.currentInputs["MOVE_LEFT"])]:
            self.rect.x -= self.speed *dt
            # If the player is flipped (facing right), then flip the player
            if self.isFlipped:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isFlipped = False
        # If the jump key is pressed, then jump
        if keys[int(self.currentInputs["JUMP"])]:
            if self.gravity == False:
                self.Jump()

    def RegisterMoves(self, keysPressed):
        currentMove = None
        if self.usingKeyboard:
            currentMove = self.RegisterMovesKeyboard(keysPressed)
        else:
            for button in range(self.joystick.get_numbuttons()):
                if self.joystick.get_button(button):
                    currentMove = self.RegisterMovesController(button)
                    break
        return currentMove

    # Registers all possible moves within the game
    def RegisterMovesKeyboard(self, keys):
        currentMove = None
        if keys[int(self.currentInputs["REGULAR_ATTACK"])]:
            currentMove = "REGULAR_ATTACK"
        elif keys[int(self.currentInputs["HEAVY_ATTACK"])]:
            currentMove = "HEAVY_ATTACK"
        elif keys[int(self.currentInputs["SPECIAL_ATTACK"])]:
            if not self.currentGaugeAmount < 50:
                currentMove = "SPECIAL_ATTACK"
        elif keys[int(self.currentInputs["ULTIMATE_ATTACK"])]:
            currentMove = "ULTIMATE_ATTACK"
        elif keys[int(self.currentInputs["VANISH"])]:
            if not self.currentGaugeAmount < 25:
                currentMove = "VANISH"
        elif keys[int(self.currentInputs["BLOCK"])]:
            currentMove = "BLOCK"
        return currentMove

    # Controller controls
    def RegisterMovesController(self, buttonPressed):
        currentMove = None

        if self.currentInputs["BLOCK"] == buttonPressed:
            currentMove = "BLOCK"
        elif self.currentInputs["REGULAR_ATTACK"] == buttonPressed:
            currentMove = "REGULAR_ATTACK"
        elif self.currentInputs["HEAVY_ATTACK"] == buttonPressed:
            currentMove = "HEAVY_ATTACK"
        elif self.currentInputs["SPECIAL_ATTACK"] == buttonPressed:
            if not self.currentGaugeAmount < 50:
                currentMove = "SPECIAL_ATTACK"
        elif self.currentInputs["ULTIMATE_ATTACK"] == buttonPressed:
            currentMove = "ULTIMATE_ATTACK"
        elif self.currentInputs["VANISH"] == buttonPressed:
            if not self.currentGaugeAmount < 25:
                currentMove = "VANISH"

        return currentMove

    # Moves the player (via controller)
    def MovePlayerController(self, dt):
        # Checks to see if the left joystick has been pressed and goes to the right, then moves right
        if self.joystick.get_axis(0) > 0.5:
            self.rect.x += self.speed *dt
            if not self.isFlipped:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isFlipped = True
        # Checks to see if the left joystick has been pressed and goes to the left, then moves left
        if self.joystick.get_axis(0) < -0.5:
            self.rect.x -= self.speed *dt
            if self.isFlipped:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isFlipped = False
        # Checks to see if the left joystick has been pressed and goes up, then jumps
        if self.joystick.get_axis(1) < -0.5:
            if self.gravity == False:
                self.Jump()

    def PerfomMove(self, currentMove, otherPlayer):
        isHit = False
        match(currentMove):
            case "REGULAR_ATTACK":
                isHit = self.RegularAttack(otherPlayer.rect)
            case "HEAVY_ATTACK":
                isHit = self.HeavyAttack(otherPlayer)
            case "BLOCK":
                self.BlockAttacks()
            case "SPECIAL_ATTACK":
                isHit = self.SpecialAttack(otherPlayer)
            case "VANISH":
                self.Vanish(otherPlayer.rect)
            case _:
                pass
        return isHit
    
    # Vanishes
    def Vanish(self, otherPlayerRect):
        # If the current player position is to the right of the opponent, then teleport to the oppoents left
        if otherPlayerRect.x < self.rect.x:
            self.rect.x = otherPlayerRect.x - (self.characterWidth * 1.5)
            self.rect.y = otherPlayerRect.y - (self.characterHeight * 1.5)
        # IF the current player position is to the left of the opponent, then teleport to the opponents right
        else:
            self.rect.x = otherPlayerRect.x + (self.characterWidth * 1.5)
            self.rect.y = otherPlayerRect.y - (self.characterHeight * 1.5)
        # Deduct 25 from the current gauge amount
        self.currentGaugeAmount -= 25

        # Adds a cooldown to the vanish move
        self.cooldownAttacks["VANISH"] = pygame.time.get_ticks() + 3000

    def RegularAttack(self, otherPlayerHitbox):
        if self.isFlipped:
            if not self.flippedAttacks["REGULAR_ATTACK"]:
                self.regularAttack = pygame.transform.flip(self.regularAttack, True, False)
                self.flippedAttacks["REGULAR_ATTACK"] = True
            self.regularAttackRect.center = (self.rect.right, self.rect.center[1])
        else:
            if self.flippedAttacks["REGULAR_ATTACK"]:
                self.regularAttack = pygame.transform.flip(self.regularAttack, True, False)
                self.flippedAttacks["REGULAR_ATTACK"] = False
            self.regularAttackRect.center = (self.rect.left, self.rect.center[1])
        self.cooldownAttacks["REGULAR_ATTACK"] = pygame.time.get_ticks() + 2000

        isHit = False
        if self.regularAttackRect.colliderect(otherPlayerHitbox):
            isHit = True
        return isHit

    def HeavyAttack(self, otherPlayer):
        if self.isFlipped:
            if not self.flippedAttacks["HEAVY_ATTACK"]:
                self.heavyAttack = pygame.transform.flip(self.heavyAttack, True, False)
                self.flippedAttacks["HEAVY_ATTACK"] = True
            self.heavyAttackRect.center = (self.rect.right, self.rect.center[1])
        else:
            if self.flippedAttacks["HEAVY_ATTACK"]:
                self.heavyAttack = pygame.transform.flip(self.heavyAttack, True, False)
                self.flippedAttacks["HEAVY_ATTACK"] = False
            self.heavyAttackRect.center = (self.rect.left, self.rect.center[1])

        self.cooldownAttacks["HEAVY_ATTACK"] = pygame.time.get_ticks() + 2000
        isHit = False
        if self.heavyAttackRect.colliderect(otherPlayer.rect):
            isHit = True
            otherPlayer.Jump()
        return isHit

    def BlockAttacks(self):
        self.isBlocking = True


    #### Displays the current attack ####
    def DisplayAttack(self, SCREEN, attackType):
        match(attackType):
            case "REGULAR_ATTACK":
                SCREEN.blit(self.regularAttack, self.regularAttackRect)
            case "HEAVY_ATTACK":
                SCREEN.blit(self.heavyAttack, self.heavyAttackRect)
            case "BLOCK":
                pygame.draw.circle(SCREEN, "blue", self.rect.center, self.rect.width, int(self.rect.width / 5))
            case "SPECIAL_ATTACK":
                SCREEN.blit(self.specialAttack, self.specialAttackRect)
            case _:
                pass
    #### Getters ####
    ### Gets the damage for the current attack ###
    def GetAttackDamage(self, attackType):
        currentDamage = 0
        match(attackType):
            case "REGULAR_ATTACK":
                currentDamage = self.regularAttackDamage
            case "HEAVY_ATTACK":
                currentDamage = self.heavyAttackDamage
            case "SPECIAL_ATTACK":
                currentDamage = self.specialAttackDamage
            case _:
                pass
        return currentDamage

    ### Gets the stun time for each attack ###
    def GetAttackStunTime(self, attackType):
        currentStunTime = 0
        match(attackType):
            case "REGULAR_ATTACK":
                currentStunTime = 1000
            case "HEAVY_ATTACK":
                currentStunTime = 2000
            case "SPECIAL_ATTACK":
                currentStunTime = 1250
            case _:
                pass
        return pygame.time.get_ticks() + currentStunTime

    #### Flipping the player when they are attacked ####
    def RotateSelf(self, isAttacked):
        currentPlayerCenter = self.rect.center
        self.currentRotation = 0
        if isAttacked:
            if self.isFlipped:
                self.currentRotation += 7
            else:
                self.currentRotation -= 7
            
            self.image = pygame.transform.rotate(self.image, self.currentRotation)
        else:
            self.image = pygame.image.load(self.imagePath).convert_alpha()
            if self.isFlipped:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (self.characterWidth, self.characterHeight))
            self.currentRotation = 0
        self.rect = self.image.get_rect(center = currentPlayerCenter)

    #### Health ####
    def ManageHealth(self):
        self.healthRect.width = self.maxHealthRect.width * (self.health / self.maxHealth)
        if self.isPlayer1:
            self.healthRect.right = self.maxHealthRect.right

    def DisplayHealth(self, SCREEN):
        pygame.draw.rect(SCREEN, "red", self.maxHealthRect)
        pygame.draw.rect(SCREEN, "green", self.healthRect)

    def ManageGauge(self):
        self.gaugeRect.width = self.maxGaugeRect.width * (self.currentGaugeAmount / self.maxGaugeAmount)
        if not self.isPlayer1:
            self.gaugeRect.right = self.maxGaugeRect.right
    def DisplayGauge(self, SCREEN):
        pygame.draw.rect(SCREEN, "black", self.maxGaugeRect)
        pygame.draw.rect(SCREEN, "blue", self.gaugeRect)

class Etai(Character):
    def __init__(self, SCREEN, pIsPlayer1, pInputType):
        super().__init__(SCREEN, pIsPlayer1, pInputType)

        # Basic stats
        self.name = "Etai"
        self.maxHealth = 1200
        self.health = 1200
        self.speed = SCREEN.get_width() / 6

        if self.isPlayer1:
            self.imagePath = "Images/players/etai_1_model.png"
            self.image = pygame.image.load(self.imagePath).convert_alpha(SCREEN)
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.imagePath = "Images/players/etai_2_model.png"
            self.image = pygame.image.load(self.imagePath).convert_alpha(SCREEN)

        self.image = pygame.transform.scale(self.image, (self.characterWidth, self.characterHeight))
        self.rect = self.image.get_rect()

        if self.isPlayer1:
            self.rect.topleft = (SCREEN.get_width() / 5, SCREEN.get_height() * 5/7)
        else:
            self.rect.topleft = (SCREEN.get_width() * 4/5, SCREEN.get_height() * 5/7)
        
        self.specialAttackDamage = 100
        self.specialAttack = pygame.image.load("Images/players/etai_special_attack.png").convert_alpha(SCREEN)
        self.specialAttack = pygame.transform.scale(self.specialAttack, (SCREEN.get_width() / 8, self.characterHeight * 3))
        if pIsPlayer1:
            self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
        self.specialAttackRect = self.specialAttack.get_rect()

        self.jumpFlames = pygame.image.load("Images/players/etai_jump_flames.png").convert_alpha(SCREEN)
        self.jumpFlames = pygame.transform.scale(self.jumpFlames, (self.characterWidth / 2, self.characterHeight / 2))
        self.jumpFlamesRect = self.jumpFlames.get_rect()

    def Jump(self):
        self.yvelocity = -self.characterHeight / 8
        self.gravity = True

    def update(self, SCREEN, dt):
        # If self.gravity is set to true, gravity is applied
        if self.gravity == True:
            self.UseGravity(dt)
            self.UseJumpFlames()
        # Checks gravity
        self.CheckGravity(SCREEN.get_height() * 10/11)
        self.CollisionDetection(SCREEN.get_width())

    def UseJumpFlames(self):
        self.jumpFlamesRect.center = (self.rect.center[0], 0)
        self.jumpFlamesRect.top = self.rect.bottom


    def DisplayEffects(self, SCREEN):
        if self.gravity:
            SCREEN.blit(self.jumpFlames, self.jumpFlamesRect)

    def SpecialAttack(self, otherPlayer):
        if self.isFlipped:
            if not self.flippedAttacks["SPECIAL_ATTACK"]:
                self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
                self.flippedAttacks["SPECIAL_ATTACK"] = True
            self.specialAttackRect.left = self.rect.right
        else:
            if self.flippedAttacks["SPECIAL_ATTACK"]:
                self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
                self.flippedAttacks["SPECIAL_ATTACK"] = False
            self.specialAttackRect.right = self.rect.left

        self.specialAttackRect.y = self.rect.y

        # 'Slams' the opposing player down
        otherPlayer.yvelocity = self.characterHeight

        self.cooldownAttacks["SPECIAL_ATTACK"] = pygame.time.get_ticks() + 1000
        self.currentGaugeAmount -= 50
        isHit = False
        if self.specialAttackRect.colliderect(otherPlayer.rect):
            # 'Slams' the opposing player down
            otherPlayer.yvelocity = self.characterHeight
            isHit = True
        return isHit

class Tane(Character):
    def __init__(self, SCREEN, pIsPlayer1, pInputType):
        super().__init__(SCREEN, pIsPlayer1, pInputType)

        # Basic stats
        self.name = "Tane"
        self.maxHealth = 1000
        self.health = 1000
        self.speed = SCREEN.get_width() / 3

        if self.isPlayer1:
            self.imagePath = "Images/players/tane_1_model.png"
            self.image = pygame.image.load(self.imagePath).convert_alpha(SCREEN)
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.imagePath = "Images/players/tane_2_model.png"
            self.image = pygame.image.load(self.imagePath).convert_alpha(SCREEN)

        self.image = pygame.transform.scale(self.image, (self.characterWidth, self.characterHeight))
        self.rect = self.image.get_rect()

        if self.isPlayer1:
            self.rect.topleft = (SCREEN.get_width() / 5, SCREEN.get_height() * 5/7)
        else:
            self.rect.topleft = (SCREEN.get_width() * 4/5, SCREEN.get_height() * 5/7)

        #Special attack setup
        self.specialAttackDamage = 100
        self.specialAttack = pygame.image.load("Images/players/tane_special_attack.png").convert_alpha(SCREEN)
        self.specialAttack = pygame.transform.scale(self.specialAttack, (SCREEN.get_width() / 5, self.characterHeight))
        #if pIsPlayer1:
            #self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
        self.specialAttackRect = self.specialAttack.get_rect()
    
    # Special attack for tane
    def SpecialAttack(self, otherPlayer):
        # If tane is flipped (i.e., the image is facing right)
        if self.isFlipped:
            # If the image for the special attack is not flipped (not facing right)
            if not self.flippedAttacks["SPECIAL_ATTACK"]:
                # Flip the image
                self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
                # Register that the special attack image is flipped
                self.flippedAttacks["SPECIAL_ATTACK"] = True
            # The rect should be on the player's right
            self.specialAttackRect.left = self.rect.right
            # Teleport the player to be in front of the attack, making a dash
            self.rect.left = self.specialAttackRect.right
        # Do the opposite if tane is not flipped (i.e., the image is facing left)
        else:
            if self.flippedAttacks["SPECIAL_ATTACK"]:
                self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
                self.flippedAttacks["SPECIAL_ATTACK"] = False
            self.specialAttackRect.right = self.rect.left
            self.rect.right = self.specialAttackRect.left
        
        # Sets the y coordinate of the special attack to be the same height as the player
        self.specialAttackRect.y = self.rect.y

        # Set the cooldown to a second
        self.cooldownAttacks["SPECIAL_ATTACK"] = pygame.time.get_ticks() + 1000
        # Reduce gauge amount
        self.currentGaugeAmount -= 50
        
        # Registers whether the other player was hit
        isHit = False
        if self.specialAttackRect.colliderect(otherPlayer.rect):
            isHit = True
        return isHit

class Neor(Character):
    def __init__(self, SCREEN, pIsPlayer1, pInputType):
        super().__init__(SCREEN, pIsPlayer1, pInputType)

        # Basic stats
        self.name = "Neor"
        self.maxHealth = 1100
        self.health = 1100
        self.speed = SCREEN.get_width() / 5

        if self.isPlayer1:
            self.imagePath = "Images/players/neor_1_model.png"
            self.image = pygame.image.load(self.imagePath).convert_alpha(SCREEN)
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.imagePath = "Images/players/neor_2_model.png"
            self.image = pygame.image.load(self.imagePath).convert_alpha(SCREEN)

        self.image = pygame.transform.scale(self.image, (self.characterWidth, self.characterHeight))

        self.rect = self.image.get_rect()

        if self.isPlayer1:
            self.rect.topleft = (SCREEN.get_width() / 5, SCREEN.get_height() * 5/7)
        else:
            self.rect.topleft = (SCREEN.get_width() * 4/5, SCREEN.get_height() * 5/7)
        
        # Special attacks
        self.specialAttackDamage = 100
        self.specialAttack = pygame.image.load("Images/players/neor_special_attack.png").convert_alpha(SCREEN)
        self.specialAttack = pygame.transform.scale(self.specialAttack, (SCREEN.get_width() / 5, self.characterHeight * 1.5))

        if pIsPlayer1:
            self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
        self.specialAttackRect = self.specialAttack.get_rect()
    def SpecialAttack(self, otherPlayer):
        if self.isFlipped:
            if not self.flippedAttacks["SPECIAL_ATTACK"]:
                self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
                self.flippedAttacks["SPECIAL_ATTACK"] = True
        else:
            if self.flippedAttacks["SPECIAL_ATTACK"]:
                self.specialAttack = pygame.transform.flip(self.specialAttack, True, False)
                self.flippedAttacks["SPECIAL_ATTACK"] = False

        self.specialAttackRect.center = self.rect.center

        self.cooldownAttacks["SPECIAL_ATTACK"] = pygame.time.get_ticks() + 1000
        self.currentGaugeAmount -= 50
        isHit = False
        if self.specialAttackRect.colliderect(otherPlayer.rect):
            isHit = True
        return isHit