from modules.screen import pauseScreen as pause

# This function is used to verify the user inputs wherever i've got to receive a Yes or Not answer from the user
# This function returns True if the user's input is "YES" (Y), returns False if it's "NOT" (N) and returns "Void" if its ENTER (nothing)
def verifyYesOrNot(msg : str) -> str:
    print(msg)
    isThisRunning = True # Variable to control the while loop
    while isThisRunning:
        userInput = str(input()).lower() # User's input into lowecase
        match userInput:
            case "y":
                isThisRunning = False # Finish the while loop
                return "True"
            case "n":
                isThisRunning = False # Finish the while loop
                return "False"
            case "":
                isThisRunning = False # Finish the while loop
                return "Void"
            case "e":
                isThisRunning = False 
                return "Cancel"
            case _:
                print("invalid option, try again")
