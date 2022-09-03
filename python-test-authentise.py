# Task 3: Program to reverse words in a string

def ReverseString(inputStr):
    """Takes an input string and completely reverses it from first character to last"""
    inputCharList = list(inputStr)
    outputCharList = inputCharList[::-1]
    outputString = ""

    for c in outputCharList:
        outputString += c
        
    return outputString


def ReverseWordsEasy(inputStr):
    """Takes an input string and reverses the words"""
    inputWordList = inputStr.split()
    reversedWordList = inputWordList[::-1]
    outputWordList = ""

    for w in reversedWordList:
        outputWordList += w
        outputWordList += " "

    return outputWordList


def ReverseWords(inputStr):
    """Reverses the words in a string without use of String.Split()"""
    inputWordList = []
    lastSpacePosition = -1
    for count, char in enumerate(inputStr):
        if char == " ":
            word = inputStr[lastSpacePosition + 1: count]
            inputWordList += [word]
            lastSpacePosition = count     
            
    inputWordList += [inputStr[lastSpacePosition + 1:]]
    
    #print("input: ", inputWordList)
    reversedWordList = inputWordList[::-1]
    #print("reversed: ", reversedWordList)
    
    outputWordsStr = ""

    for w in reversedWordList:
        outputWordsStr += w
        outputWordsStr += " "

    return outputWordsStr

def main():
    stringIdxs = []
    flagIdxs = []
    flag = ""
    
    print("Please enter a string in quotes '' or "", with a flag - -r or -w: ")
    userInput = input()
    
    for count, char in enumerate(userInput):
        if char == "'" or char == '"':
            stringIdxs += [count]
        if char == "-":
            flagIdxs += [(count + 1)]

    stringStartIdx = min(stringIdxs)
    stringEndIdx = max(stringIdxs)

    userInputStr = userInput[stringStartIdx + 1 : stringEndIdx]
        
    flagIdxs = [x for x in flagIdxs if x > stringEndIdx] # Only a '-' outside the input string can be the flag

    if len(flagIdxs) > 0:
        flag = userInput[max(flagIdxs)]
    else:
        raise Exception("No flag specified")

    if flag == "r":
        resultToPrint = ReverseString(userInputStr)
    elif flag == "w":
        resultToPrint = ReverseWords(userInputStr)
    else:
        raise Exception("Only flags -r and -w are allowed")

    print(resultToPrint)

if __name__ == "__main__":
    main()