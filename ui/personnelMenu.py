from tabulate import tabulate
from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br
from modules.personnel.add import addPersonnel

titlePersonnel = """
        ******************
        * Personnel menu *
        ******************
"""

def personnelMenu():
    while True:
        clean()
        print(titlePersonnel)
        print('')
        print('Select the number according to the action you want to do')
        print('')
        personnelOptions = [['1.' ,'Add'], ['2.','Edit'], ['3.','Delete'], ['4.','Search'], ['5.','Return']] # Options the user can get in.
        print(tabulate(personnelOptions, tablefmt='youtrack')) # Use tabulate to render a table using the options of the activeOptions list.
        selectedOp = str(input())
        if selectedOp == "1": # If user's input is "1" then call the addActive function.
            addPersonnel()
        elif selectedOp == "2": # If user's input is "2" then call the editActive function.
            pass
        elif selectedOp == "3":
            pass
        elif selectedOp == "4":
            pass
        elif selectedOp == "5":
            return
        else: # If the user doesn't type a valid option.
            print('Please select a valid option...')
            pause()