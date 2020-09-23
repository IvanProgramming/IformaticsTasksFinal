a = int(input())
sum_ = 0
while a > 0:
    sum_ += a % 10
    a //= 10
print(sum_)
