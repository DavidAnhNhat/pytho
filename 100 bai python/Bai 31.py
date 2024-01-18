a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
if a > b:
    for k in range(1, a + 1):
        if a % k == 0 and b % k == 0:
            print(k)
elif b > a:
    for k in range(1, b + 1):
        if a % k == 0 and b % k == 0:
            print(k)
