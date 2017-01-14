from random import randint
import os

# Function to fetch the user name from file and return his/her points
try:
    def getUserPoint(userName):
        inputFile = open("userScores.txt", 'r')
        content = []
        for line in inputFile: # convert the input data into list type(per line)
            content.append(line.split(','))
            # print (content, "\n")
        for i in content: # check whether the given name(userName) exist in the data or not
            if userName == i[0]:
                inputFile.close()
                return i[0], i[1]
        inputFile.close()
        return -1


    # Function to update the points of old user and create a new entry for new user
    def updateUserPoints(newUser, userName, score):
        if newUser == True:  # New user entry in data file
            inputFile = open("userScores.txt", 'a')
            inputFile.write("\n")
            inputFile.write(userName)
            inputFile.write(", ")
            inputFile.write(str(score))
            inputFile.close()

        elif newUser == False:  # User already exists
            tempFile = open("userScores.tmp", 'w')
            inputFile = open("userScores.txt", 'r')
            content = []
            for line in inputFile:  # convert the input data into list type(per line)
                content = (line.split(','))
                if userName == content[0]:
                    content[1] = score
                    tempFile.write(content[0])
                    tempFile.write(", ")
                    tempFile.write(str(content[1]))
                else:
                    tempFile.write(line)  # copying the data to a temporary file for update
                print(line)
            tempFile.close()
            inputFile.close()
        os.rename("userScores.tmp", "userScores1.txt")
except IOError:
    print ("File not found with this name. A new file will be created now!")
    inputFile = open("userScores.txt", 'w')
    inputFile.close()


def generateQuestion():
    # apply the BODMAS arithmetic
    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "**"}
    for i in range(len(operandList)):
        operandList[i] = randint(1, 9)
    for i in range(len(operatorList)):
        if "**" not in operatorList:
            operatorList[i] = operatorDict[randint(1, 4)]
        elif "**" in operatorList:
            operatorList[i] = operatorDict[randint(1, 3)]
    # Generating the question string
    questionString = ""
    questionString += str(operandList[0])
    for i in range(4):
        questionString += str(operatorList[i])
        questionString += str(operandList[i + 1])
    # Evaluating the question string to get answer of the expression
    result = int(eval(questionString))
    # Interacting with user
    print("Your Question is:", questionString.replace("**", "^"))
    userReply = 0
    while True:
        try:
            userReply = int(input("Answer is: "))
            break
        except:
            print("ERROR! answer should be a numeric value")
    if userReply == result:
        print("Well done! Correct answer :) ")
        return 5
    if userReply != result:
        print("Sorry, Wrong answer :(")
        print("The correct answer is:", result)
        return 0

