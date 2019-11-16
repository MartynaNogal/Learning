def main():
    pass

if __name__ == '__main__':
    main()

#You, the user, will have in your head a number between 0 and 100.
#The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

def Game():
    step = 0
    l = range(101)
    center = int(len(l)/2)
    while True:
        step += 1
        guess = str(input("Is your number is %.0f? (Y/N) " %l[center]))

        if guess == "N":
            num = int(input("Is mine number %.0f is too high(1)/too low(2) than yours?" %l[center]))

            if num == 2:

                l = l[center:len(l)]
                center = int(len(l)/2)

            elif num == 1:

                l = l[0:center]
                center = int(len(l)/2)

        elif guess == "Y":
            print("Your number is: ", l[center])
            print("I do it in %.0f steps." % step)
            break

Game()