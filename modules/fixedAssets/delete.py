from modules.files import checkFile, loadFile, updateFile
from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.verifyFunctions.yesOrNot import verifyYesOrNot

# This function is used to delete an asset with a given transaction code
def deleteAsset():
    isDeleteAssetRunning : bool = True # Variable to control the while loop
    while isDeleteAssetRunning:
        clean()
        checkFile("assets.json")
        assetsData = loadFile("assets.json") # Load the assets.json data into a variable
        print("Type the transaction code of the asset you want to delete")
        codeToDelete = str(input()) # Receive the code of the asset that the user wants to delete
        if codeToDelete not in assetsData: # If the code doesn't exist
            clean()
            print("Couldn't find the code... please try again")
            pause()
            continue
        clean()
        print("This is all the information of the transaction code you typed")
        br()
        for key in assetsData[codeToDelete]:
            if key != "history":
                print(f"{key} : {assetsData[codeToDelete][key]}")
        br()
        message = "Press (Y) if you want to delete this asset\nPress (N) if you don't want to delete this asset"
        userYesOrNot = verifyYesOrNot(message)
        if userYesOrNot != "True":
            clean()
            print("The asset will not be deleted...")
            pause()
            return
        assetsData.pop(codeToDelete)
        updateFile("assets.json",assetsData)
        clean()
        print("Asset deleted succesfully...")
        pause()
        isDeleteAssetRunning = False
        break
            