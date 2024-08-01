from tabulate import tabulate
from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.fixedAssets.add import addAsset
from modules.fixedAssets.edit import editAsset
from modules.fixedAssets.delete import deleteAsset
from modules.fixedAssets.search import searchAsset

titleAsset = """
        ***************
        * Assets menu *
        ***************
"""

def assetMenu():
    while True:
        clean()
        print(titleAsset)
        print('')
        print('Select the number according to the action you want to do')
        print('')
        activeOptions = [['1.' ,'Add'], ['2.','Edit'], ['3.','Delete'], ['4.','Search'], ['5.','Return']] # Options the user can get in.
        print(tabulate(activeOptions, tablefmt='youtrack')) # Use tabulate to render a table using the options of the activeOptions list.
        selectedAct = str(input())
        if selectedAct == "1": # If user's input is "1" then call the add asset function.
            addAsset()
        elif selectedAct == "2": # If user's input is "2" then call the edit asset function.
            editAsset()
        elif selectedAct == "3": #If user's input is "3" then call the delete asset function
            deleteAsset()
        elif selectedAct == "4": # If user's input is "4" then call the search asset function
            searchAsset()
        elif selectedAct == "5": # If user's input is "5" then return to main menu
            return
            break
        else: # If the user doesn't type a valid option.
            print('Please select a valid option...')
            pause()
        
        