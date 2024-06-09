from ui.mainMenu import *

if __name__ == '__main__':
    while True:
        try:
            mainMenu()
            break
        except KeyboardInterrupt:
            clean()
            print("Don't break this code >:C")
            pause()