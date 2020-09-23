a, b = map(int, input().split())
res = []

for i in range(a, b + 1):
    # How does it works?
    # Firstly, we convert i**2(square of i) to str.
    # Secondly counting the length of i in symbols (before this action, i converts to str)
    # Finally cutting the length of i from i**2 in str
    if str(i**2)[-(len(str(i))):] == str(i):
        res.append(i)

if res:
    print(*res)
else:
    print("-1")


