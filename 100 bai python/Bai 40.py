n = int(input())
tong = 0
while n > 0:
    so = n % 10
    tong += so
    n //= 10
print("Tong chu so la:", tong)