def main():
    pass

if __name__ == '__main__':
    main()

def TicTacToe(size):
    horizontal = [" ---"]
    vertical = ["|  "]
    count = 0
    while True:
        print (''.join(horizontal*size))
        print (' '.join(vertical*(size+1)))
        count += 1
        if count == size:
            break
    print (''.join(horizontal*size))

size = int(input("Size your TicTacToe: "))
TicTacToe(size)
