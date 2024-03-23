#Longest Collatz Sequence
biggest=0
biggest_num=0
for i in range(4,1000001):
    counter=1
    num = i
    while num!=1:
        if num%2==0:
            num=num/2
        else:
            num=3*num+1
        counter+=1
    if counter>biggest:
        biggest=counter
        biggest_num=i
print(biggest_num)


