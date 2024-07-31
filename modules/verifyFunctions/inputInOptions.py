from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

def isInputInOptions(options : list, mainItem : str) -> str:
    isThisRunning = True
    while isThisRunning:
        clean()
        print(mainItem)
        br()
        print("Please type one of the following options")
        br()
        for item in options:
            print(item)
        br()
        userInput = str(input()).lower()
        inputInOptions = False
        for item in options:
            if userInput == item.lower():
                inputInOptions = True
                isThisRunning = False
                clean()
                return userInput
        if inputInOptions == False:
            br()
            print("Please verify your answer and try again...")
            pause()
        