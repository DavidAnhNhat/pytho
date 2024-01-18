n = int(input("Nhap so n:"))
chan = 0
le = 0
dem = 0
def dem(n):
    while n != 0:
        
        n //= 10
        dem += 1
        break
print(dem)
        