#Sum Square Diffrance
sum=0
sqr=0
for i in range (1,101):
    sum=i*i+sum
    sqr=sqr+i
sqr=sqr*sqr
print(sqr-sum)