#Lattice Path
right=20
down=20

# my solve (obviously it's the bad one)
def pathCalc(right_x,down_x): #recursive - it might(certainly) take a long time
    if right_x == 0 or down_x == 0:
        return 1
    else:
        return pathCalc(right_x-1,down_x) + pathCalc(right_x,down_x-1)

# better way to solve
def pathCalc2(right_x, down_x): #dynamic - very fast

    table = [[0] * (down_x + 1) for _ in range(right_x + 1)]
    for i in range(right_x + 1):
        for j in range(down_x + 1):
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[right_x][down_x]

print(pathCalc2(right,down))

