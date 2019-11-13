def main():
    pass

if __name__ == '__main__':
    main()

#Create a program that will play the “cows and bulls” game with the user.
import random
def c_b():
    numb = random.sample(range(10),4) #creat random choise number from(range 0 to 10, population = 4)
    while True:
        guess = input("Your guess: ")
        user = []
        for i in guess: #i is in order number from ouer guess
            user.append(int(i)) #add every i to list "user"
            cow = 0

        for i in range(4): #i is in order range 0 to 3
            if numb[i] == user[i]: #if numb[i pozition in list] = user[i pozition in list]
                cow += 1

        bull = 0
        for i in range(4):
            for j in range(4):
                if numb[i] == user [j]:
                    bull += 1

        print("cow: ", cow,"bull: ", bull)
        if numb == user:
            print("You win! Numer is: ", numb)
            break

c_b()