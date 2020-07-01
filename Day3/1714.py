a = int(input())
b = int(input())

count = 0
for n in range(a, b + 1):
    flag = True
    for i in range(2, int(n**0.5) + 1):
        if(n % i == 0):
            flag = False
            break
    if(n == 1):
        flag = False
    if(flag):
        count += 1

print(count)