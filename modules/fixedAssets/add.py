from modules.screen import cleanScreen as clean, pauseScreen as pause
from modules.files import *
from modules.verifyFunctions.inputInOptions import isInputInOptions
from modules.verifyFunctions.applianceTypes import verifyApplianceTypes
from modules.verifyFunctions.verifyBrands import verifyBrands
from modules.verifyFunctions.computerTypes import verifyComputerTypes

# This function is used to insert an active from the user into the assets.json file
def addAsset():
    clean()
    checkFile('assets.json') # Check if the assets.json exists and if it doesn't create it 
    assetsData = loadFile('assets.json') # Bring the json data into a variable
    assets = { # Create the main structure our assets are going to have
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
    for item in assets: # Use a for loop to go through every structure's item 
        if item != "history": # Checks the "history" so the for loop doesn't create an input for it
            if item in numberOptions:
                while True:
                    try:
                        while True:
                            clean()
                            newValue =  int(input(f'Enter {item}: ')) # Store the new value from an input for each item
                            if item == "transactionCode":
                                if str(newValue) in assetsData:
                                    clean()
                                    print("This transactionCode already exists, please enter a new one")
                                    pause()
                                    continue
                                else:
                                    break
                            break
                        assets[item] = newValue # Update the main structure with the new value 
                        break
                    except:
                        clean()
                        print(f'Please enter a valid number for {item}')
                        pause()
            else:
                clean()
                if item == "brand":
                    newValue = verifyBrands(item)
                elif item == "category":
                    categoryOptions = ["Computer Equipment","Appliance"]
                    newValue = isInputInOptions(categoryOptions,item)
                elif item == "type":
                    match assets["category"]:
                        case "appliance":
                            newValue = verifyApplianceTypes()
                        case "computer equipment":
                            newValue = verifyComputerTypes()
                else:
                    newValue =  input(f'Enter {item}: ') # Store the new value from an input for each item
                assets[item] = newValue # Update the main structure with the new value
    # Once the for loop ends
    code = assets["transactionCode"] # Bring the transaction code that's going to be the main id for the json file
    assetsData.update({code : assets}) # Update the assetsData we loaded from the json file
    updateFile('assets.json', assetsData) # Update the json file with the new assets structure
        

