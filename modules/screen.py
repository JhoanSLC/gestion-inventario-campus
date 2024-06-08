import os 
import sys

# Clean screen depending on wich OS you're using
def cleanScreen():
    if sys.platform == 'linux': # If the OS is Linux then use the linux's clear command
        os.system('clear')
    else: # If it is windows then use the win's cls command
        os.system('cls')

# Pause screen depending on wich OS you're using

def pauseScreen():
    if sys.platform == 'linux':
        input('Press any key to continue...')
    else:
        os.system('pause')