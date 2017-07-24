def array_left_rotation(a, n, k):
    b = []
    for i, val in enumerate(a):
        b.append(a[(i + k) % len(a)] )
    return b

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
