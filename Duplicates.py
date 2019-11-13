def main():
    pass

if __name__ == '__main__':
    main()

#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
def li(n):
    c = list(set(n))
    print(c)

#set() - it take the element which don't be duplicated

def li2(n):
    c = []
    for i in n:
        if i not in c:
            c.append(i)
    print(c)

t = [1,1,1,2,2,22,2,25,5,45,876,78,888,8,8,8,8,8]
li(t)
li2(t)
