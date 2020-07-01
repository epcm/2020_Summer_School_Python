n = int(input())

sum = 0
for i in range(1, n + 1):
    if (not ('7' in str(i)) and not (i % 7 == 0)):
        sum += i

print(sum)