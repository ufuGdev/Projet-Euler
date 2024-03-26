#Maximum Path Sum I
with open("txts/018.txt", "r") as file:
    lines = file.readlines()

num = [[int(num) for num in line.strip().split(" ") if num] for line in lines if line.strip()]

for i in range(len(num) - 2, -1, -1):
    for j in range(len(num[i])):
        num[i][j] += max(num[i+1][j], num[i+1][j + 1])

print(num[0][0])
