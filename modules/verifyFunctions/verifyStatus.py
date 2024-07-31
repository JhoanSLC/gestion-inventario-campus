from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

def verifyStatus() -> str:
    isThisRunning = True
    while isThisRunning:  
        clean()
        br()
        statusOptionsToShow = ["0. Not assigned", "1. Assigned","2. Retired","3. Warranty repair"]
        statusOptionsNumbers = ["0","1","2","3"]
        print("Please type the status of this asset (has to be one of the numbers below)")
        br()
        for item in statusOptionsToShow:
            print(f'{item}')
        br()
        userInput = str(input()).lower()
        if userInput not in statusOptionsNumbers:
            br()
            print("Please verify the status and try again...")
            pause()
            continue
        isThisRunning = False
        return userInput