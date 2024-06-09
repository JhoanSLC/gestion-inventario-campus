from tabulate import tabulate
from modules.actives.activesMain import *

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
        options = [['1.' ,'Actives'], ['2.','Staff'], ['3.','Zones'], ['4.','Active assignment'], ['5.','Reports'], ['6.','Movimientos de Activos'], ['7.','Salir']]
        print(tabulate(options, tablefmt='youtrack'))
        selected = str(input())
        
        if selected == "1":
            activesMenu()
        elif selected == "2":
            pass
        elif selected == "3":
            pass
        elif selected == "4":
            pass
        elif selected == "5":
            pass
        elif selected == "6":
            pass
        elif selected == "7":
            clean()
            print('Come back soon...')
            break
        