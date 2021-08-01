# Dikdörtgen çevresini ve alanını bul

while True:
    try:
        x0 = int(input("Dikdörtgenin uzun kenarını giriniz: "))
        x1 = int(input("Dikdörtgenin kısa kenarını giriniz: "))
        if x0 > x1:
            break
        else:
            print("***Uzun kenar kısa kenardan kısa veya eşit olamaz***\n***Tekrar deneyiniz***")
    except ValueError:
        continue

perimeter = 2*(x0 + x1)
area = x0*x1

print("Çevre", perimeter)
print("Alan", area)
