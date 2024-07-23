from modules.files import checkFile, loadFile, updateFile
from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

# This function is used to delete an active with a given transaction code
def deleteActive():
    isDeleteActiveRunning : bool = True # Variable to control the while loop
    while isDeleteActiveRunning:
        clean()
        checkFile("actives.json")
        activesData = loadFile("actives.json") # Load the actives.json data into a variable
        print("Type the transaction code of the active you want to delete")
        codeToDelete = str(input()) # Receive the code of the active that the user wants to delete
        if codeToDelete not in activesData: # If the code doesn't exist
            print("Couldn't find the code... please try again")
            pause()
            continue
        

            