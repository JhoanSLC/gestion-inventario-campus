from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.files import *
from modules.verifyFunctions.yesOrNot import verifyYesOrNot
from modules.verifyFunctions.intOptions import verifyIntOptions

# This function is used to edit a or some values of an active
def editActive():
    clean()
    checkFile("actives.json") # Check if the actives.json file exists
    activesData = loadFile("actives.json") # Load all the json file data inside the variable

    codeToEdit = str(input("Type the transaction code of the active you want to edit\n")) # Ask for the transaction code so i know wich active the user wants to change
    if codeToEdit not in activesData:
        clean()
        print("The transaction code doesn't exist in the database")
        pause()
    else:
        clean()
        nonEditableOptions = ["transactionCode","history"] # List of the options the user can't change
        numberOptions : list = ["formNumber", "campusCode", "unitValue","serialNumber"] # List of number options
        for k in activesData[codeToEdit]:
            if k not in nonEditableOptions: # Make sure the user is not able to change some options
                clean()
                print(f"{k}") # Show the current option being iterated in the for loop
                br()
                userYesOrNot = verifyYesOrNot() # Call the function that verifies the "yes or not" questions (modules.verifyFunctions.yesOrNot)
                if userYesOrNot == "True":
                    clean()
                    message : str = "Type the new value keeping in mind if the value has to be a number or not"
                    if (k in numberOptions): # If the current option is a number type
                        newValue = verifyIntOptions(message) # Use the function that verifies the input to make sure it is a number
                        activesData[codeToEdit][k] = newValue # Replace the current value with the new one
                    else: # If it's not a  number type option
                        print(message)
                        newValue = str(input()) # Ask the new string value
                        activesData[codeToEdit][k] = newValue # Replace the current value with the new one
                elif userYesOrNot == "Void": # If the verify yes or not function returns a "Void"
                    return # Cancel the proccess qand return to the actives menu


    updateFile("actives.json", activesData) # Once all the process is finished update the actives.json with the new values        


    


