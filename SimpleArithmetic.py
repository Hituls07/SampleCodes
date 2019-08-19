
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))


class Calculator:

    def __init__(self, lst):
        self.lst = lst
        self.size = len(lst)

    def mean(self):
        total = 0
        for i in self.lst:
            total += i

        return round(total / self.size, 1)

    def median(self):
        self.lst.sort()
        if self.size % 2 != 0:
            return self.lst[int((self.size + 1) / 2) - 1] # Because python indexes starts with 0
        else:
            middle = int((self.size + 1) / 2) - 1 # Because python indexes starts with 0
            return (self.lst[middle] + self.lst[middle + 1]) / 2

    def mode(self):
        self.lst.sort()
        highest = 0
        value = 0
        for num in self.lst:
            if self.lst.count(num) > highest:
                highest = self.lst.count(num)
                value = num

        return value


calc = Calculator(arr)
print(calc.mean())
print(calc.median())
print(calc.mode())
