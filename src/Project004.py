#Largest Palindrome Product
result=0
for i in range(100, 1000):
    for j in range(100, 1000):
        x=i*j
        if(str(x)[::-1]==str(x) and x>result):
            result=x

print(result)