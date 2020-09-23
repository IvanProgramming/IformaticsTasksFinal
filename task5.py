def is_all_digits_equal(n: int):
  base = n % 10
  while n > 0:
    if base != n % 10:
      return False
    n //= 10
  return True
a = int(input())
if is_all_digits_equal(a):
  print("YES")
else:
  print("NO")
