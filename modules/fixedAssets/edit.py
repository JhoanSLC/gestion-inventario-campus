from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.files import *
from modules.verifyFunctions.yesOrNot import verifyYesOrNot
from modules.verifyFunctions.intOptions import verifyIntOptions

# This function is used to edit a or some values of an asset
def editAsset():
    clean()
    checkFile("assets.json") # Check if the assets.json file exists
    assetsData = loadFile("assets.json") # Load all the json file data inside the variable

    codeToEdit = str(input("Type the transaction code of the asset you want to edit\n")) # Ask for the transaction code so i know wich asset the user wants to change
    if codeToEdit not in assetsData:
        clean()
        print("The transaction code doesn't exist in the database")
        pause()
    else:
        clean()
        nonEditableOptions = ["transactionCode","history","category","type","status"] # List of the options the user can't change
        numberOptions : list = ["formNumber", "campusCode", "unitValue","serialNumber"] # List of number options
        for k in assetsData[codeToEdit]:
            if k not in nonEditableOptions: # Make sure the user is not able to change some options
                clean()
                print(f"{k}") # Show the current option being iterated in the for loop
                br()
                message = "Press (Y) if you want to change this value\nPress (N) if you want to skip this value\nPress (ENTER) if you want to send the update\nPress (E) to cancel the update"
                userYesOrNot = verifyYesOrNot(message) # Call the function that verifies the "yes or not" questions (modules.verifyFunctions.yesOrNot)
                if userYesOrNot == "True":
                    clean()
                    message : str = "Type the new value keeping in mind if the value has to be a number or not"
                    if (k in numberOptions): # If the current option is a number type
                        newValue = verifyIntOptions(message) # Use the function that verifies the input to make sure it is a number
                        assetsData[codeToEdit][k] = newValue # Replace the current value with the new one
                    else: # If it's not a  number type option
                        print(message)
                        newValue = str(input()) # Ask the new string value
                        assetsData[codeToEdit][k] = newValue # Replace the current value with the new one
                elif userYesOrNot == "Void": # If the verify yes or not function returns a "Void"
                    break # Cancel the proccess qand return to the assets menu
                elif userYesOrNot == "Cancel":
                    return

    updateFile("assets.json", assetsData) # Once all the process is finished update the assets.json with the new values        


    


