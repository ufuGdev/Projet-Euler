#Power Digit Sum
x=2**1000
y=str(x)
x=0
for i in range(len(y)):
    x+=int(y[i])
print(x)