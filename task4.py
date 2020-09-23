def find_nearby_duplicates(n: int) -> bool:
    """
    :param n: Integer to inspect
    :return: True, if integer has 2 equal neighbour digits
    """
    prev = 0
    while n > 0:
        if prev == n % 10:
            return True
        else:
            prev = n % 10
            n //= 10
    return False


a = int(input())
if find_nearby_duplicates(a):
    print("YES")
else:
    print("NO")
