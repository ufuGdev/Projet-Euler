#Even Fibonacci Numbers
f1,f2=1,1
sum=0
while f2<4000000:
    if f2%2==0:
        sum+=f2
    f1,f2=f2,f1+f2
print(sum)
