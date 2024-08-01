from modules.files import *
from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.verifyFunctions.yesOrNot import verifyYesOrNot


def searchAsset():
    isSearchAssetRunning : bool = True # Variable to control the while loop
    while isSearchAssetRunning:
        clean()
        checkFile("assets.json")
        assetsData = loadFile("assets.json") # Load the assets.json data into a variable
        print("Type the transaction code of the asset you want to see")
        codeToSearch : str = str(input()) # Receive the code of the asset that the user wants to delete
        if codeToSearch not in assetsData: # If the code doesn't exist
            clean()
            print("Couldn't find the code... please try again")
            pause()
            continue
        clean()
        print("This is all the information of the transaction code you typed")
        br()
        for key in assetsData[codeToSearch]: # Go through every key in the assets json file
            if key != "history":
                print(f"{key} : {assetsData[codeToSearch][key]}") # Show the key being iterated and the value of that key
        br()
        pause()
        clean()
        print("Do you want to search another asset?")
        message : str = "Type (Y) if you want to search another asset\nType (N) if you don't want to search another asset\n"
        userInput : str = verifyYesOrNot(message)
        if userInput != "True":
            isSearchAssetRunning = False
            return