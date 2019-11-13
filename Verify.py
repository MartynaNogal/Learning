def main():
    pass

if __name__ == '__main__':
    main()

###Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
###The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
def verify(num,l):
    center = int(len(l)/2)
    step = 0
    #from list[length(list)/2)]
    while True:
        step += 1
        if num == l[center]: #when number = center number in list:
            print("Number %.0f is in the list." % num)
            print(step)
            break
        elif num > l[center]: #when number is > than list center:
            l = l[center:len(l)]  #new list = list[from center : to length(old list)]
            center = int(len(l)/2) #new center from new list
        else:
            l = l[0:center] #new list = list[from zero : to center]
            center = int(len(l)/2) #new list = list[from center : to length(old list)]

number = int(input("What number you looking for: "))
listt = sorted(range(0,1000))
verify(number, listt)