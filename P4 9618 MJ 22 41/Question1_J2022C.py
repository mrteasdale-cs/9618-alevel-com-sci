fileData = [["",""] for i in range(11)]

def ReadHighScores():
    with open("HighScore.txt", "r") as file:
        print()
        for i in range(0,10):
            fileData[i][0] = file.readline()[:3]
            fileData[i][1] = file.readline()
    file.close()

def OutputHighScores():
    for i in range (len(fileData)):
        print(fileData[i][0].strip("\n"), fileData[i][1].strip())

ReadHighScores()
OutputHighScores()

player = input("Enter player name: ")
while len(player) != 3:
    player = input("Must be 3 characters, enter player name: ")

score = int(input("Enter score: "))
while 1 > score > 100000:
    score = input("Must be an integer between 1-100000. Enter score: ")

for i in range(0, 10):
    currScore = int(fileData[i][1]) #5000 > 2000
    if score > currScore:

        for j in range(10, i, -1):
            fileData[j] = fileData[j - 1]

        fileData[i][0] = player
        fileData[i][1] = str(score)
        break

OutputHighScores()




