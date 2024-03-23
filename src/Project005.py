#Smallest Multiple
i=2520
while(1):
    f = 1
    for j in range(11,21):
        if(i%j!=0):
            f = 0
            break
    if f == 1:
        break
    i = i + 2520
print(i)