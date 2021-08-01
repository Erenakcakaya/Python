# Hipotenüs hesaplama
import math

x0 = float(input("Bir dik kenar giriniz: "))
x1 = float(input("Diğer dik kenarı giriniz: "))

hypotenuse = math.sqrt((x0*x0)+(x1*x1))

print("Hipotenüs:", hypotenuse)
