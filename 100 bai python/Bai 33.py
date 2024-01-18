import math
a = int(input("Nhap so a:"))

for k in range(2, int(math.sqrt(a)) + 1 ):
    if a % k == 0:
        print("Khong phai la so nguyen to")
        break
else:
    print("La so nguyen to")
