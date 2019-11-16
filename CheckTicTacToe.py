def main():
    pass

if __name__ == '__main__':
    main()

matrix = [[0,0,0] for i in range(3)]

while True:
    for i in matrix:
        print (i)

    pl1 = input("Player 1, your move: ").split()
    while True:
        if matrix[int(pl1[0])][int(pl1[1])] == 0:
            matrix[int(pl1[0])][int(pl1[1])] = 1
            break
        else:
            pl1 = input("Wrong! Player 1, your move: ").split()

    for i in matrix:
        print (i)

    pl2 = input("Player 2, your move: ").split()
    while True:
        if matrix[int(pl2[0])][int(pl2[1])] == 0:
            matrix[int(pl2[0])][int(pl2[1])] = 1
            break
        else:
            pl2 = input("Wrong! Player 2, your move: ").split()

    for i in range(1,3):
        if i == matrix[0][0] and matrix[1][1] and matrix[2][2]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[0][2] and matrix[1][1] and matrix[2][0]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[0][0] and matrix[0][1] and matrix[0][2]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[1][0] and matrix[1][1] and matrix[1][2]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[2][0] and matrix[2][1] and matrix[2][2]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[0][0] and matrix[1][0] and matrix[2][0]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[0][1] and matrix[1][1] and matrix[2][1]:
            print("Pl nr %.0f win." %i)
            break
        elif i == matrix[0][2] and matrix[1][2] and matrix[2][2]:
            print("Pl nr %.0f win." %i)
            break