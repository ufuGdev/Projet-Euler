#Summation of Primes
sum=2
for i in range(3,2000000,2):
    f=1
    for j in range(2,int(i ** 0.5)+1):
        if i%j==0:
            f=0
            break
    if f==1:
        sum=sum+i
print(sum)
