def main():
    pass

if __name__ == '__main__':
    main()


import random
file = []
with open('sowpods.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        file.append(str(line.replace("\n", "")))
        line = open_file.readline()

while True:
    los = list(random.choice(file))
    n = len(los)
    print(los)
    guess = list("_"*n)

    print("Welcome to Hangman!")
    print(" ".join(guess))

    list_count = [len(los)]
    lose = 0
    hangman = ["---\n  |","---\n  |\n  O","---\n  |\n  O\n  |","---\n  |\n  O\n \|","---\n  |\n  O\n \|/","---\n  |\n  O\n \|/ \n /","---\n  |\n  O\n \|/\n / \ "]

    while True:
        letter = str(input("Guess your letter: "))
        letter = letter.upper()
        count = 0
        for i in range(len(los)):
            if guess[i] == letter:
                print("Try to guess a letter again!")
                letter = str(input("Guess your letter: "))
            if los[i] == letter:
                guess[i] = letter
            if guess[i] == "_":
                count += 1
        list_count.append(count)
        print(" ".join(guess))

        for i in range(len(list_count)-2,len(list_count)-1):
            if list_count[i] == list_count[i+1]:
                lose += 1
        print("You have %.0f guesses left." %(6-lose))
        print(hangman[lose])

        if lose == 6:
            print("You guessed 6 letters incorrectly. You lose!")
            break

        if los == guess:
            print("Congratulation! The word is", "".join(guess))
            break


    end = str(input("Play again? "))
    end = end.upper()
    if end == "N":
        print("Thanks for the game!")
        break



