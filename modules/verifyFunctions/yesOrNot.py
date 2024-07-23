from modules.screen import pauseScreen as pause

# This function is used to verify the user inputs wherever i've got to receive a Yes or Not answer from the user
# This function returns True if the user's input is "YES" (Y), returns False if it's "NOT" (N) and returns "Void" if its ENTER (nothing)
def verifyYesOrNot() -> str:
    print("Press (Y) if you want to change this value\nPress (N) if you want to skip this value\nPress (ENTER) if you want to cancel")
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
            case _:
                print("invalid option, try again")
