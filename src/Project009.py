#Special Pythagorean Triplet
for a in range(1,1000):
    for b in range(1,a):
        c=int((a**2+b**2) ** 0.5)
        if a+b+c==1000 and a**2+b**2==c**2:
            print(a*b*c)
i*i