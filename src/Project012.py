#Highly Divisible Triangular Number
subcounter =0
counter=0
for i in range(1,100000):
    counter=0
    subcounter+=i
    for j in range(1,int(subcounter**0.5)+1):
        if subcounter % j == 0:
            counter += 2
            if j == int(subcounter**0.5):
                counter -= 1
    if counter > 500:
        print(subcounter)
        break