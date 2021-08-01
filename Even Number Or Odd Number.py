#Girilen sayı tek mi çift mi bulma

print("Sayıyı giriniz: ", end="")
x = int(input())

if x%2 == 0:
    print(x, "sayısı çifttir")
else:
    print(x, "sayısı tektir")
