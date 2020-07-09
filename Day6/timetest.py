import time
import math
from matplotlib import pyplot as plt
x = []
y = []

def Fibonacci(n):
    if n in (1, 2):
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

for n in range(1, 35):
    count = 0
    start_time = time.time()
    f = Fibonacci(n)
    end_time = time.time()
    print(f'Fibonacci({n}) = {f} required   {end_time-start_time}')
    x.append(n)
    y.append(end_time-start_time)

plt.xlabel("n") 
plt.ylabel("time") 
plt.plot(x,y) 
plt.show()