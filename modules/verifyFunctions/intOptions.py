from modules.screen import cleanScreen as clean, pauseScreen as pause

# This function is used to verify if the user input is a number when the data type has to be a number
# Receive: The message you want to show to the user
def verifyIntOptions(message : str) -> int:
    isThisRunning : bool = True # Variable to control the while loop
    while isThisRunning:
        clean()
        print(message)
        try:
            newValue = int(input()) # Ask the user for the new value
            isThisRunning = False # If everything's fine. Change the control variable to false so the while loop doesn't keep running
            return newValue # Finally return the user's new value

        except Exception:
            print("Please, try again")
            pause()
            

