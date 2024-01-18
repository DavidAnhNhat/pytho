a = int(input("Nhap so a:"))
s = 0
for k in range(1, a + 1):
    if a % k == 0:
        s += 1
print(s)
