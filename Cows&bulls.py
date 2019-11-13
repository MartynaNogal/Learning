def main():
    pass

if __name__ == '__main__':
    main()

#Create a program that will play the “cows and bulls” game with the user.
import random
def c_b():
    numb = random.sample(range(0,10),4)
    print(numb)
    while True:
        guess = input("Your guess: ")
        user = []
        for i in guess:
            user.append(int(i))
            cow = 0

        for i in range(0,4):
            for j in range(0,4):
                if numb[i] == user[i]:
                    cow += 1

        bull = 0
        for i in range(0,4):
            for j in range(0,4):
                if numb[i] == user [j]:
                    bull += 1

        print("cow: ", cow,"bull: ", bull)
        if numb == user:
            print("You win! Numer is: ", numb)
            break

c_b()