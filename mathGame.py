import functions as fn

try:
    userName = input("Enter your name: ")
    userScore = int(fn.getUserPoint(userName))
    newUser = False
    if userScore == -1:
        newUser = True
        userScore = 0
    userChoice = 0
    while (userChoice != -1):
        marks = fn.generateQuestion()
        userScore += marks
        userReply = input("Do you want a next question. Y or N: ")
        if userReply == "y" or "Y":
            userChoice = 0
        if userReply == "n" or "N":
            userChoice = -1
            break
    fn.updateUserPoints(newUser, userName, userScore)

except Exception as e:
    print (e)
