from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

def verifyComputerTypes() -> str:
    isThisRunning = True
    while isThisRunning:
        clean()
        print("Please enter the type of computer equipment")
        br()
        computerOptions = ["Monitor", "CPU","Keyboard","Mouse"]
        for item in computerOptions:
            print(f'* {item}')
        userInput = str(input('\n')).lower()
        br()
        for item in computerOptions:
            if item.lower() == userInput.lower():
                isThisRunning = False
                return userInput
        print("Please verify your answer and try again...")
        pause()