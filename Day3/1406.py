n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += str(i).count('1')

print(sum)
