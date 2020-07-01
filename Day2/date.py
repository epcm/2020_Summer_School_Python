y = int(input())
m = int(input())
n = int(input())

if((m in [1, 3, 5, 7, 8, 10, 12] and n in range(1, 32)) or (m in [4, 6, 9, 11] and n in range(1, 31)) or (m == 2 and (n in range(1, 29) or (((y%4 == 0 and y % 100 !=0) or y %400 ==0) and n == 29)))):
    print("Yes")
else:
    print("No")