def has_equal_digits(n: int):
  dig_arr = []
  while n > 0:
    if n % 10 not in dig_arr:
      dig_arr.append(n % 10)
    else:
      return True
    n //= 10
  return False


a = int(input())
if has_equal_digits(a):
  print("YES")
else:
  print("NO")
