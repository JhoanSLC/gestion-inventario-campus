from modules.screen import cleanScreen as clean, pauseScreen as pause, breakLine as br

# This function is used on personnel add function and it verifies that the document type is a valid one
def verifyDocumentTypes() -> str: 
    isThisRunning = True
    while isThisRunning:
        clean()
        documentTypes = { # List of valid document types
            "1" : "Passport",
            "2" : "National ID Card",
            "3" : "Driver's License",
            "4" : "Residence Permit",
            "5" : "Social Security Card",
            "6" : "Birth Certificate",
            "7" : "Voter ID Card",
            "8" : "Military ID",
            "9" : "Foreigner's ID Card",
            "10" : "Refugee Travel Document",
            "11" : "Employment Authorization Document (EAD)"
        }
        print("Please type the number according to the document type of the person you are adding")
        br()
        for key in documentTypes:
            print(f'{key}. {documentTypes[key]}')
        userInput = str(input())
        if userInput not in documentTypes:
            br()
            print("Please verify your answer and try again...")
            pause()
            continue
        return documentTypes[userInput]
    
