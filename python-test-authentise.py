# Task 4: Take the input string as a file name

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
    
    reversedWordList = inputWordList[::-1]
    
    outputWordsStr = ""

    for w in reversedWordList:
        outputWordsStr += w
        outputWordsStr += " "

    return outputWordsStr

def ParseString(userInput):
    stringIdxs = []
    flagIdxs = []
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

    return userInputStr, flag

def ReadFile(path):
    filepath = fr"{path}"
    
    try:
        
        with open(filepath) as f:
            lines = f.readlines()
        f.close()
        pass
    except:
        print("The requested file could not be found. Please specify the full path and name including extension")
    
    for line in lines:
        #print("Line found with length ", len(line))
        if len(line) > 1: # Empty lines prior to message will have length of 1, skip these
            outputStr = line
            break
        
    return outputStr

def main():
    outputFromFile = ""
    flag = ""

    print("Please enter the filepath and name of a .txt file including its extension: ")
    
    inputPath = input()
    
    outputFromFile = ReadFile(inputPath)
    
    inputStr, flag = ParseString(outputFromFile)
    
    if flag == "r":
        resultToPrint = ReverseString(inputStr)
    elif flag == "w":
        resultToPrint = ReverseWords(inputStr)
    else:
        raise Exception("Only flags -r and -w are allowed")

    print(resultToPrint)

if __name__ == "__main__":
    main()