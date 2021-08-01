# İki sayıyı karşılaştır

x0 = int(input("İlk sayıyı giriniz: "))
x1 = int(input("İkinci sayıyı giriniz: "))

if x0 < x1:
    print(x0, "sayısı", x1, "sayısından küçüktür")
elif x0 == x1:
    print(x0, "sayısı", x1, "sayısı birbirine eşittir")
else:
    print(x0, "sayısı", x1, "sayısından büyüktür")
