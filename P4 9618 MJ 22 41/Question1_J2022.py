fileData = [["",""] for i in range(10)]
#fileData = [["FYI",10000],["ABC", 9092]]
global count
def ReadHighScores():
    with open("HighScore.txt", "r") as file:
        print()
        for i in range(0,10):
            fileData[i][0] = file.readline()[:3].strip("\n")
            fileData[i][1] = file.readline().strip()
    file.close()

def OutputHighScores():
   for i in range(0,len(fileData)): #iterator i
       print(fileData[i][0].strip("\n"), fileData[i][1])

def topTen(player, score):
   count = 1
   for i in range(len(fileData)):
       curr_score = fileData[i][1]
       if int(score) > int(curr_score):
           temp1 = fileData[i][0]
           temp2 = fileData[i][1]
           fileData[i][0] = player
           fileData[i][1] = score
           count += 1
           while (count < 10):
               next1 = fileData[count][0]
               next2 = fileData[count][1]
               fileData[count][0] = temp1
               fileData[count][1] = temp2
               temp1 = next1
               temp2 = next2
               count += 1
           break

def writeTopTen():
    with open("NewHighScore.txt", "w") as file:
        for i in range(0,10):
            line = str(fileData[i][0].strip("\n")) + " " + str(fileData[i][1]) + "\n"
            file.write(line)

ReadHighScores()
OutputHighScores()

player = "A"
while len(player) != 3:
    player = input("Enter player name: ")

score = -1
while score < 1 or score > 100000:
    score = int(input("Enter score: "))

topTen(player, score)

OutputHighScores()
writeTopTen()
