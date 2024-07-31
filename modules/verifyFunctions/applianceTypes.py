from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

def verifyApplianceTypes() -> str:
    isThisRunning = True
    while isThisRunning:
        clean()
        print("Please enter the type of appliance")
        br()
        applianceOptions = ["Air conditioner", "printer","tv"]
        for item in applianceOptions:
            print(item)
        userInput = str(input()).lower()
        br()
        for item in applianceOptions:
            if item.lower() == userInput.lower():
                isThisRunning = False
                return userInput
        br()
        print("Please verify your answer and try again...")
        pause()