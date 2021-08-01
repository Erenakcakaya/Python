
# 4000000 milyonun altındaki Fibonaacci sayılarının toplamı
x = 0
y = 1

while x < 4000000:
    total = x + y - 1
    print(x)
    res = x + y
    x = y
    y = res

print("Toplam:", total)
