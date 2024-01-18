def tim_gia_tri_xa_nhat(L, x):
    min_value = min(L)
    max_value = max(L)
    if x >= min_value and x <= max_value:
        return x
    elif x < min_value:
        return max_value
    else:
        return min_value

L = []
x = int(input("Nhập số nguyên x: "))
for i in range(int(input("Nhập số phần tử trong list: "))):
    L.append(int(input("Nhập phần tử thứ {}: ".format(i + 1))))
print(tim_gia_tri_xa_nhat(L, x))
