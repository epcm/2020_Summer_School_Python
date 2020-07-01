n = int(input())
x = int(input())
y = int(input())
a = y//x
b = y%x
if b != 0:
    a += 1
print(n - a)