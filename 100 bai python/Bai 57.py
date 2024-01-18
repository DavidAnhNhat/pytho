n = int(input())
a = []
for k in range(0, n):
    a.append(int(input()))
s = max(a)

so_dau = a[0]
def find_max_negative(d):
  return max(a for a in d if a < 0)
print(find_max_negative(n))    
