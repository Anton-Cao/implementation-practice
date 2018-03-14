import unittest

class Heap():
    def __init__(self, values=[],key=lambda x: x):
        self.values = values
        self.key = key
        self.index = 0
        for i in range(len(values) - 1, -1, -1):
            self.heapify_down(i)

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        try:
            return self.values[key]
        except Exception as e:
            raise(e)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.values[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def sort(self):
        res = []
        while len(self.values) > 0:
            res.append(self.pop())
        self.values = res
        return res

    def push(self, v):
        self.values.append(v)
        self.heapify_up(len(self.values) - 1)

    def top(self):
        return self.values[0]

    def pop(self):
        min = self.values[0]
        self.s(0, len(self.values) - 1)
        self.values.pop()
        self.heapify_down(0)
        return min

    def heapify_up(self, i):
        if self.p(i) >= 0:
            node = self.values[i]
            par = self.values[self.p(i)]
            if self.key(par) > self.key(node):
                self.s(i, self.p(i))
                self.heapify_up(self.p(i))

    def heapify_down(self, i):
        if i < len(self.values):
            node = self.values[i]
            left_child = None
            right_child = None
            if self.l(i) < len(self.values):
                left_child = self.values[self.l(i)]
            if self.r(i) < len(self.values):
                right_child = self.values[self.r(i)]
            if right_child != None and self.key(right_child) < self.key(left_child) and self.key(right_child) < self.key(node):
                self.s(i, self.r(i))
                self.heapify_down(self.r(i))
            elif left_child != None and self.key(left_child) < self.key(node):
                self.s(i, self.l(i))
                self.heapify_down(self.l(i))
            
    def s(self, i, j):
        try:
            temp = self.values[i].deepcopy()
            self.values[i] = self.values[j]
            self.values[j] = temp
        except:
            self.values[i], self.values[j] = self.values[j], self.values[i]
    
    def p(self, i):
        return (i - 1) // 2

    def l(self, i):
        return 2 * i + 1

    def r(self, i):
        return 2 * i + 2


class TestHeap(unittest.TestCase):
    def test_01(self):
        '''
        Test heap creation
        '''
        h = Heap([10, 3, 2, 8, 5, 7, 1, 6, 4, 9])
        res = True
        for i in range(1, len(h)):
            if h.values[h.p(i)] > h.values[i]:
                res = False
        self.assertTrue(res)

    def test_02(self):
        '''
        Test indexing
        '''
        h = Heap([1, 0])
        res = h[0] == 0 and h[1] == 1
        self.assertTrue(res)

    def test_03(self):
        '''
        Test insertion
        '''
        h = Heap()
        h.push(5)
        h.push(3)
        h.push(1)
        res = h.values == [1, 5, 3]
        self.assertTrue(res)

    def test_04(self):
        '''
        Test sort
        '''
        a = Heap([3, 1, 4, 1, 5, 9, 2]).sort()
        res = True
        for i in range(1, len(a)):
            res &= a[i] >= a[i-1]
        self.assertTrue(res)

if __name__ == "__main__":
    res = unittest.main(verbosity = 3, exit = False)
