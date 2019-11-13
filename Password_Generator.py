def main():
    pass

if __name__ == '__main__':
    main()

#Password Generator
import random
def password(power,long):
    if power == 1:
        passw_w = [chr(i) for i in range(97,122)] #create list [set chr(from i) when i is in order numb from range: 97 to 121]; chr translator from ascii to text
        passw_w = ''.join(str(x) for x in (random.sample(passw_w,long))) #join with '' empty gap (str(from x) when x is in order (random choise(from pazzw_w, population = long)
        print("Your weak password is: ", passw_w)
    elif power == 2:
        haslo_m = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,122)]
        haslo_m = ''.join(str(x) for x in (random.sample(haslo_m,long)))
        print("Your medium password is: ", haslo_m)
    elif power == 3:
        haslo_s = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,122)] + list(range(0,11)) + ["_", "-"]
        haslo_s = ''.join(str(x) for x in (random.sample(haslo_s,long)))
        print("Your strong password is: ", haslo_s)

power = input("How strong do you want the password? (1.weak, 2.medium, 3.strong): ")
long = int(input("How long do you want the password? "))
password(power, long)