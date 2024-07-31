from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

def verifyBrands(mainItem : str) -> str:
    isThisRunning = True
    while isThisRunning:  
        clean()
        print(mainItem)
        br()
        brandOptions = ["lg", "compumax","logitech","benq","asus","lenovo","hp"]
        print("Please type the brand of this asset (has to be one of the brands below)")
        br()
        for item in brandOptions:
            print(f'* {item}')
        br()
        userInput = str(input()).lower()
        if userInput not in brandOptions:
            br()
            print("Please verify the brand and try again...")
            pause()
            continue
        isThisRunning = False
        return userInput
