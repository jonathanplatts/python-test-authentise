# Task 2: Program to reverse words in a string
# Add task 1 to a function for use later

def ReverseString(userInput):
    userInput = input()

    inputCharList = list(userInput)
    outputCharList = inputCharList[::-1]
    outputString = ""

    for c in outputCharList:
        outputString += c
    
    print(outputString)
    
def main():
    print("Please enter a sentence: ")

    userInput = input()

    ## Easy way
    # inputWordList = userInput.split()
    # reversedWordList = inputWordList[::-1]
    # outputWordList = ""

    # for w in reversedWordList:
    #     outputWordList += w
    #     outputWordList += " "

    # print(outputWordList)

    ## And without String.Split()...

    inputWordList = []
    lastSpacePosition = -1
    for count, char in enumerate(userInput):
        if char == " ":
            word = userInput[lastSpacePosition + 1: count]
            inputWordList += [word]
            lastSpacePosition = count     
            
    inputWordList += [userInput[lastSpacePosition + 1:]]
        
    reversedWordList = inputWordList[::-1]
    outputWordsStr = ""

    for w in reversedWordList:
        outputWordsStr += w
        outputWordsStr += " "

    print(outputWordsStr)
    
if __name__ == "__main__":
    main()