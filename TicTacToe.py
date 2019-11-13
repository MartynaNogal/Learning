def main():
    pass

if __name__ == '__main__':
    main()

def TicTacToe(size):
    horizontal = [" ---"]
    vertical = ["|  "]
    count = 0
    while True:
        print (''.join(horizontal*size)) #join list * size with '' empty gap
        print (' '.join(vertical*(size+1))) #join list * size+1 (one more in vertical) with ' ' gap
        count += 1
        if count == size: #when count = size -> STOP
            break
    print (''.join(horizontal*size)) #print one more horizontal at the end

size = int(input("Size your TicTacToe: "))
TicTacToe(size)
