from tabulate import tabulate
from ui.assetsMenu import *
from ui.personnelMenu import personnelMenu

# Title to print in console
mainTitle = """ 
        ************************************************
        * WELCOME TO CAMPUSLAND'S INVENTORY MANAGEMENT *
        ************************************************
"""
def mainMenu():
    while True:
        clean()
        print(mainTitle)
        print('')
        print('Select the number according to the section you want to access')
        print('')
        options = [['1.' ,'Assets'], ['2.','Personnel'], ['3.','Zones'], ['4.','Asset assignment'], ['5.','Reports'], ['6.','Assets history'], ['7.','Exit']] # List of the main menu options
        print(tabulate(options, tablefmt='youtrack'))
        selected = str(input())
        
        if selected == "1": # If user's input is "1" calls the assets menu
            assetMenu()
        elif selected == "2": # If user's input is "2" calls the personnel menu
            personnelMenu()
        elif selected == "3":
            pass
        elif selected == "4":
            pass
        elif selected == "5":
            pass
        elif selected == "6":
            pass
        elif selected == "7": # If user's input is "7" then close the program
            clean()
            print('Come back soon...')
            break
        