a =float(input("Nhap diem toan:"))
b = float(input("Nhap diem van:"))
c = float(input("Nhap diiem anh:"))
d = ( a + b + c) / 3
while ( a > 10 or  b > 10 or  c > 10 or d > 10):
    print("Hay nhap lai diem")
    if 0 < a < 10 and 0 < b < 10 and 0 < c < 10:
        break

if d >= 8 and a >= 8 or  b >= 8 and a >= 6.5 and b >= 6.5 and c >= 6.5:
    print("Hoc sinh gioi")
elif d >= 6.5 and a >= 6.5 or b >= 6.5 and a <= 5 and b <= 5 and c <= 5:
    print("Hoc sinh kha")
elif d >= 5 and a >= 5 or b >= 5 and a >= 3.5 and b >= 5 and c >= 5:
    print("Hoc sinh trung binh")
else:
    print("Hoc sinh kem")

