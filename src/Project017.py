#Number Letter Counts
def num_to_word(x):
    if x==0:
        return ""
    if x == 1:
        return "one"
    if x == 2:
        return "two"
    if x == 3:
        return "three"
    if x == 4:
        return "four"
    if x == 5:
        return "five"
    if x == 6:
        return "six"
    if x == 7:
        return "seven"
    if x == 8:
        return "eight"
    if x == 9:
        return "nine"
    if x == 10:
        return "ten"
    if x == 11:
        return "eleven"
    if x == 12:
        return "twelve"
    if x == 13:
        return "thirteen"
    if x == 14:
        return "fourteen"
    if x == 15:
        return "fifteen"
    if x == 16:
        return "sixteen"
    if x == 17:
        return "seventeen"
    if x == 18:
        return "eighteen"
    if x == 19:
        return "nineteen"
    if 20 <= x < 30:
        return "twenty"+num_to_word(x%10)
    if 30 <= x < 40:
        return "thirty"+num_to_word(x % 10)
    if 40 <= x < 50:
        return "forty"  + num_to_word(x % 10)
    if 50 <= x < 60:
        return "fifty"  + num_to_word(x % 10)
    if 60 <= x < 70:
        return "sixty"  + num_to_word(x % 10)
    if 70 <= x < 80:
        return "seventy"+num_to_word(x % 10)
    if 80 <= x < 90:
        return "eighty"+num_to_word(x % 10)
    if 90 <= x < 100:
        return "ninety"+num_to_word(x % 10)
    if 100 <= x < 1000:
        if x % 100 == 0:
            return num_to_word(x // 100) + "hundred"
        else:
            return num_to_word(x // 100) + "hundredand" + num_to_word(x % 100)
    if x == 1000:
        return "onethousand"
x=''
for i in range(1,1001):
    x+=num_to_word(i)
print(len(x)) # a bit rough around the edges but it'll do