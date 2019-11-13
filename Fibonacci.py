def main():
    pass

if __name__ == '__main__':
    main()

def Fibonacci(n):
    if n == 0:      #for 0 Fibonacci number = 0
        c = [0]
    elif n == 1:    #for 1 Fibonacci number = 1
        c = [0, 1]
    else:           #for other numbers
        count = 0
        c = [0, 1]
        while count != (n-1):   #when count is not n-1
            c.append((c[count]+c[count+1])) #add to list (Fibonacci n - 1 + Fibonacci n - 2)
            count += 1
    print("The string for %s numbers is: %s" %(n, c))

number = int(input("For how many numbers should the Fibonacci series be created? "))
Fibonacci(number)