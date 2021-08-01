# Sinüs teoremi ile üçgen alanı hesaplama
import math

x0 = float(input("Kenar uzunluğunu giriniz: "))
x1 = float(input("Diğer kenar uzunluğunu giriniz: "))
x2 = float(input("İki kenar arasındaki açıyı giriniz giriniz: "))

pi = 3.14
area = x0*x1*math.sin(x2*pi/180)/2

print("Alan:", area)
