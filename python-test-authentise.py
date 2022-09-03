# Task 1: Program to reverse a string

print("Please enter a string: ")

userInput = input()

inputCharList = list(userInput)
outputCharList = inputCharList[::-1]
outputString = ""

for c in outputCharList:
    outputString += c
    
print(outputString)
