# Class that manages player inputs
class PlayerKeyboardInput:
    # Gets the corresponding player input from the text file
    def GetCurrentInputs(isPlayer1):
        playerInputs = {}
        
        txtName = "player2KeyboardInput.txt"
        if isPlayer1:
            txtName = "player1KeyboardInput.txt"
        
        with open(txtName, "r") as file:
            for line in file.readlines():
                # Splits the string by the colon, then seperates each value (removing the \n on the second variable)
                # Then puts it all into a dictionary
                lineSplit = line.split(":")
                playerInputs.update({lineSplit[0]:lineSplit[1].rstrip()})
        return playerInputs
    
    # Writes the corresponding player input into the text file
    def WriteCurrentInput(action, rebindKey, isPlayer1):
        # Gets the entire list of player inputs and changes the rebind key with its corresponding action
        playerInputs = PlayerKeyboardInput.GetCurrentInputs(isPlayer1)
        playerInputs[action] = rebindKey
        
        txtName = "player2KeyboardInput.txt"
        if isPlayer1:
            txtName = "player1KeyboardInput.txt"

        with open(txtName, "w") as file:
            for key in playerInputs.keys():
                # Keys are represented in ASCII value
                file.write(key + ":" + str(playerInputs[key]) + "\n")

class PlayerControllerInput:
    def GetCurrentInputs():
        buttonInputs = {}

        txtName = "playerControllerInput.txt"
        
        with open(txtName, "r") as file:
            for line in file.readlines():
                # Splits the string by the colon, then seperates each value (removing the \n on the second variable)
                # Then puts it all into a dictionary
                lineSplit = line.split(":")
                buttonInputs.update({lineSplit[0]: int(lineSplit[1])})
        return buttonInputs

        
    def WriteCurrentInput(action, rebindKey, isPlayer1):
        # Gets the entire list of player inputs and changes the rebind key with its corresponding action
        playerInputs = PlayerControllerInput.GetCurrentInputs(isPlayer1)
        playerInputs[action] = rebindKey
        
        txtName = "player2KeyboardInput.txt"
        if isPlayer1:
            txtName = "player1KeyboardInput.txt"

        with open(txtName, "w") as file:
            for key in playerInputs.keys():
                # Keys are represented in ASCII value
                file.write(key + ":" + str(playerInputs[key]) + "\n")