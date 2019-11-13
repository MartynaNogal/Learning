def main():
    pass

if __name__ == '__main__':
    main()


#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.
def rev():
    n = str(input("Write string: "))
    print(" ".join(n.split()[::-1])) #print (join with " " gap(string.split()[::-1])) [::-1] backwards
rev()