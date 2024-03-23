#Maximum Path Sum I
f= open("txts/018.txt", "r")
lenght=0
sum=0
for i in range(15):
    lenght+=2
    biggest=0
    str = f.readline()
    for j in range(0,lenght,2):
        x=int(str[j] + str[j+1])
        if x>biggest:
            biggest=x
    sum+=biggest
    print(sum)

