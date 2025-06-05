# CIE COMPUTER SCIENCE 9618/42
# MayJune Series
# Q1 - Mr Teasdale
WordArray = []
NumberWords = 0

def ReadWords(file_name):
    global WordArray
    global NumberWords

    with open(file_name) as file:
        for line in file:
            WordArray.append(line.strip())
            NumberWords += 1

    play()

def play():
    global WordArray
    global NumberWords
    print(f"The main word is {WordArray[0]}. Number of answers {NumberWords}")
    user_guess = ""
    correct = 0
    while user_guess != "no":
        user_guess = input("Enter your guess: ")

        if user_guess in WordArray:
            print("That's correct!")
            WordArray[WordArray.index(user_guess)] = "null"
            correct += 1
        else:
            print("Try again.")

    print(f"You got {correct} correct answers!")
    print(f"Missed answers include")
    for word in WordArray:
        if word != "null":
            print(word)

if __name__ == '__main__':
    difficulty = input("Enter a difficulty (easy. medium, hard): ").capitalize()
    ReadWords(difficulty + ".txt")


