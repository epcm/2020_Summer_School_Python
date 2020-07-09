class MyList(list):

    def product(self):
        mul = self[0]
        for i in self[1:]:
            mul *= i
        return mul

    def __add__(self, other):
        if len(self) != len(other):
            print('Check Your list!')
            raise ValueError
        ls = MyList()
        for a, b in zip(self, other):
            ls.append(a + b)
        return ls

    def __mul__(self, other):
        if len(self) != len(other):
            print('Check Your list!')
            raise ValueError
        ls = MyList()
        for a, b in zip(self, other):
            ls.append(a * b)
        sum = 0
        for i in ls:
            sum += i
        return sum

ls = MyList([3, 5, 7, 9])
print(f'ls = {ls}')
print(f'ls.product() = {ls.product()}\n')

ls1 = MyList(['5', 7, '4'])
ls2 = MyList(['9sd', 4, '1ss'])
print(f'ls1 = {ls1}\nls2 = {ls2}')
print(f'ls1 + ls2 = {ls1 + ls2}\n')

ls1 = MyList([2, 4, 6])
ls2 = MyList([3, 5, 9])
print(f'ls1 = {ls1}\nls2 = {ls2}')
print(f'ls1 * ls2 = {ls1 * ls2}\n')

ls1 = MyList([2, 4, 6])
ls2 = MyList([3, 5, 9, 4])
print(f'ls1 = {ls1}\nls2 = {ls2}')
print(f'ls1 * ls2 = {ls1 * ls2}')