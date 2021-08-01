
# Birden bine kadar olan sayılar arasındaki hem 3'e hem 5'e bölünebilen sayılar
x = 1
while x <= 1000:
    if x % 3 == 0 or x % 5 == 0:
        print(x)
    x = x + 1
