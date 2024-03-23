#Largest Prime Factor
x=600851475143
i = 3
biggest = 0
while i * i <= x:
    if x % i == 0:
        x = x // i
        biggest = i
    else:
        i += 1
if x > biggest:
    biggest = x

print("The largest is", biggest)