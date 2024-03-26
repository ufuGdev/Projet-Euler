#Largest Product in a Grid
with open("txts/011.txt", "r") as file:
    lines = file.readlines()

x = [[int(num) for num in line.strip().split(" ") if num] for line in lines if line.strip()]
biggest=0

#horizontal
for i in range(20):
    for j in range(17):
        mul = x[i][j]*x[i][j+1]*x[i][j+2]*x[i][j+3]
        if mul>biggest:
            biggest = mul

#vertical
for i in range(17):
    for j in range(20):
        mul = x[i][j]*x[i+1][j]*x[i+2][j]*x[i+3][j]
        if mul>biggest:
            biggest = mul

#diagonal "\" type
for i in range(17):
    for j in range(17):
        mul = x[i][j]*x[i+1][j-1]*x[i+2][j-2]*x[i+3][j-3]
        if mul>biggest:
            biggest = mul

#diagonal "/" type
for i in range(3,20):
    for j in range(17):
        mul = x[i][j]*x[i-1][j-1]*x[i-2][j-2]*x[i-3][j-3]
        if mul>biggest:
            biggest = mul

print(biggest)
