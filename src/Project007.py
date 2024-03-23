#10001st Prime
x=3
counter=1
while True:
    f=1
    for i in range(2,x//2):
        if(x%i==0):
            f=0
            break
    if f==1:
        counter+=1
        if counter==10001:
            print(x)
            break
    x += 2



