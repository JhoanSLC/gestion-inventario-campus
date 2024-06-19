import os
import json

BASE = 'DATA/'

# Create a json file if it does not exist
# Receive: Json file name
def checkFile(file : str):
    if not os.path.isfile(BASE+file): # Checks if the file exists and if it doesn't then the function creates it
        with open (BASE+file, 'w') as createFile:
            json.dump({},createFile, indent = 4)
    
# Load a json file into a python variable
# Receive: Json file name
def loadFile(file : str):
    with open (BASE+file, 'r') as readFile:
        return json.load(readFile)
    
# Send a new data to the json file
# Receive: Json file name and the data you will add to that json
def updateFile(file : str, data):
    with open (BASE+file, 'w+') as updateFile:
        json.dump(data, updateFile, indent = 4)