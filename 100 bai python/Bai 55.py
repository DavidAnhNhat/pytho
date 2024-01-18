
n = int(input())
a = []
for k in range(0, n):
    a.append(int(input()))

def check_equal(n):
  so_dau = a[1]
  for so in a:
    if so != so_dau:
      return False
  return True 
print(check_equal(n))