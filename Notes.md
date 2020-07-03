### Python数据类型

<img src="C:\Users\张开元\AppData\Roaming\Typora\typora-user-images\image-20200630162949106.png" alt="image-20200630162949106" style="zoom: 67%;" />

#### int float

int不限制大小

浮点数17位 注意作差判相等`round(0.2+0.1, 10) == round(0.3, 10)`

进制转换：`bin() oct() hex()`

整型：`oct(233)`

浮点数：`(2.33).oct()`

可进行连续比较`1 <= m < n <= 10`

#### 赋值语句

`a = b = c = d`

`a, b, c = 7, 8, 9`

#### 字符串的操作

```python
split 分割 join 合并
upper/lower/swapcase 大小写相关
ljust/center/rjust (总位数)
replace(str, str)
```

<img src="C:\Users\张开元\AppData\Roaming\Typora\typora-user-images\image-20200701174152921.png" alt="image-20200701174152921" style="zoom:50%;" />



#### list的操作

<img src="C:\Users\张开元\AppData\Roaming\Typora\typora-user-images\image-20200701183049217.png" alt="image-20200701183049217" style="zoom:67%;" />

#### tuple的构建

t = ('sss',) # 一定要有',' 因为()的特殊性，建立list时','可有可无

#### dict与set

set是没有value的dict，同为hash实现，故有很高的检索效率，也因此dict中可用in检索key

key必须为不可变类型

#### print的可选参数

sep = " ", end = '\n'

读入数据：一行多个整数值
	alist = list(map(int, input().split()))