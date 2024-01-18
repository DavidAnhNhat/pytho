def tim_gia_tri_duong_dau_tien(L):
    return min(L) if min(L) > 0 else -1

L = [-1, -2, 0, 3, 4]
print(tim_gia_tri_duong_dau_tien(L))