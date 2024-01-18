def count_digits(n):
  k = 0
  while n != 0:
    n //= 10
    k += 1
  return k
n = int(input("Hay nhap so n:"))

print(count_digits(n))
