def main():
    pass

if __name__ == '__main__':
    main()

#Make a two-player Rock-Paper-Scissors game.
pl1 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
pl2 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
while True:
    if pl1 - pl2 == 0:
        print("Draw!")
        q = input("Do you want play again? (Y/N)")
        if q == "N":
            print("Thanks for game ;)")
            break
        else:
            pl1 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
            pl2 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
    elif pl1 - pl2 == 1 or pl1 - pl2 == -2:
        print("Player number 1 won!")
        q = input("Do you want play again? (Y/N)")
        if q == "N":
            print("Thanks for game ;)")
            break
        else:
            pl1 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
            pl2 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
    else:
        print("Player number 2 won!")
        q = input("Do you want play again? (Y/N)")
        if q == "N":
            print("Thanks for game ;)")
            break
        else:
            pl1 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))
            pl2 = int(input("Select 1.Rock, 2.Paper, 3.Scissors! "))