n = int(input())
step = 0
while n != 1:
    if n % 2 == 1:
        n = int(3 * n + 1)
    else:
        n //= 2
    print(n)
    step += 1
print('\n', step, sep = '')