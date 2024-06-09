from tabulate import tabulate
from .addActives import *
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
        activeOptions = [['1.' ,'Add'], ['2.','Edit'], ['3.','Delete'], ['4.','Search'], ['5.','Return']]
        print(tabulate(activeOptions, tablefmt='youtrack'))
        selectedAct = str(input())
        if selectedAct == "1":
            addActives()
        elif selectedAct == "2":
            pass
        elif selectedAct == "3":
            pass
        elif selectedAct == "4":
            pass
        elif selectedAct == "5":
            return
            break
        else:
            print('Please select a valid option...')
            pause()
        
        