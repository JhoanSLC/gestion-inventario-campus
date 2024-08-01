from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

def verifyPhones():
    isThisRunning = True
    while isThisRunning:
        clean()
        phonesOptions = {
            "1" : "mobile",
            "2" : "home",
            "3" : "personal",
            "4" : "office"
        }
        print("Type the phone you want to add for this person")
        for item in phonesOptions
