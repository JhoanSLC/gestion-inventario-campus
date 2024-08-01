from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.files import loadFile
from modules.files import updateFile
from modules.files import checkFile
from modules.verifyFunctions.personnel.documentTypes import verifyDocumentTypes

def addPersonnel():
    isThisRunning = True
    while isThisRunning:
        clean()
        checkFile("personnel.json") # verify if personnel.json exists and creates it if it doesn't
        personnelStructure = { # Main structure of personnel
            "id" : "",
            "documentType" : "",
            "name" : "",
            "phones" : {}
        }
        toAddValue : str # Variable that will contain the value for each item of the structure
        for item in personnelStructure: # Go through every structure's key    
            if item != "phones" and item != "documentType":
                toAddValue = str(input(f'type the {item}: ')) # Store the user's input into the variable toAddValue
            elif item == "documentType": # If the item being iterated is document type
                toAddValue = verifyDocumentTypes() # then call the function to verify the valid document types
                clean()
            elif item == "phones":
                pass
            personnelStructure[item] = toAddValue # Add the user's input into the personnel structure    
                