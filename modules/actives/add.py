from modules.screen import cleanScreen as clean, pauseScreen as pause
from modules.files import *

# This function is used to insert an active from the user into the actives.json file
def addActives():
    clean()
    checkFile('actives.json') # Check if the actives.json exists and if it doesn't create it 
    activesData = loadFile('actives.json') # Bring the json data into a variable
    actives = { # Create the main structure our actives are going to have
        "transactionCode" : "",
        "formNumber" : "",
        "campusCode" : "",
        "brand" : "",
        "category" : "",
        "type" : "",
        "unitValue" : 0,
        "provider" : "",
        "serialNumber" : "",
        "responsibleCompany" : "",
        "status" : "", 
        "history" : [],
    }
    numberOptions = ["transactionCode",'formNumber','campusCode','serialNumber',"unitValue"]
    for item in actives: # Use a for loop to go through every structure's item 
        if item != "history": # Checks the "history" so the for loop doesn't create an input for it
            if item in numberOptions:
                while True:
                    try:
                        while True:
                            clean()
                            newValue =  int(input(f'Enter {item}: ')) # Store the new value from an input for each item
                            if item == "transactionCode":
                                if str(newValue) in activesData:
                                    clean()
                                    print("This transactionCode already exists, please enter a new one")
                                    pause()
                                    continue
                                else:
                                    break
                            break
                        actives[item] = newValue # Update the main structure with the new value 
                        break
                    except:
                        clean()
                        print(f'Please enter a valid number for {item}')
                        pause()
            else:
                clean()
                newValue =  input(f'Enter {item}: ') # Store the new value from an input for each item
                actives[item] = newValue # Update the main structure with the new value
    # Once the for loop ends
    code = actives["transactionCode"] # Bring the transaction code that's going to be the main id for the json file
    activesData.update({code : actives}) # Update the activesData we loaded from the json file
    updateFile('actives.json', activesData) # Update the json file with the new active structure
        

