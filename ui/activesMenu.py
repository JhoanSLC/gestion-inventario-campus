from tabulate import tabulate
from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.actives.add import addActives
from modules.actives.edit import editActive

titleActive = """
        ****************
        * Actives menu *
        ****************
"""

def activesMenu():
    while True:
        clean()
        print(titleActive)
        print('')
        print('Select the number according to the action you want to do')
        print('')
        activeOptions = [['1.' ,'Add'], ['2.','Edit'], ['3.','Delete'], ['4.','Search'], ['5.','Return']] # Options the user can get in.
        print(tabulate(activeOptions, tablefmt='youtrack')) # Use tabulate to render a table using the options of the activeOptions list.
        selectedAct = str(input())
        if selectedAct == "1": # If user's input is "1" then call the addActive function.
            addActives()
        elif selectedAct == "2": # If user's input is "2" then call the editActive function.
            editActive()
        elif selectedAct == "3":
            pass
        elif selectedAct == "4":
            pass
        elif selectedAct == "5":
            return
            break
        else: # If the user doesn't type a valid option.
            print('Please select a valid option...')
            pause()
        
        