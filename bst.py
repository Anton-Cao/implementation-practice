import unittest

'''With guidance from 6.006 example'''

class BST():
    def __init__(self, _key, _par=None, _left=None, _right=None):
        '''Initialize node of BST'''
        self.key = _key
        self.par = _par
        self.left = _left
        self.right = _right

    def minimum(self):
        '''Find node with smallest key in current subtree'''
        if self.left:
            return self.left.minimum()
        return self

    def maximum(self):
        '''Find node with largest key in current subtree'''
        if self.right:
            return self.right.maximum()
        return self

    def find(self, key):
        '''Returns a highest node having key in current subtree'''
        if self.key == key:
            return self
        elif self.key > key and self.left:
            return self.left.find(key)
        elif self.key < key and self.right:
            return self.right.find(key)
        else:
            return None

    def successor(self):
        '''Return node in tree with next larger key'''
        if self.right:
            return self.right.minimum()
        else:
            par = self.par
            while par:
                if par.key > self.key:
                    return par
                par = par.par
            return None

    def predecessor(self):
        '''Return node in tree with next smaller key'''
        if self.left:
            return self.left.maximum()
        else:
            par = self.par
            while par:
                if par.key < self.key:
                    return par
                par = par.par
            return None

    def insert(self, key):
        '''Insert node'''
        if self.key is None:
            self.key = key
            self.maintain()
        elif self.key < key:
            if self.right is None:
                self.right = self.__class__(None, self)
            self.right.insert(key)
        else:
            if self.left is None:
                self.left = self.__class__(None, self)
            self.left.insert(key)

    def maintain(self):
        pass

    def replace(self, node):
        self.key = node.key
        self.left = node.left
        self.right = node.right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def delete(self):
        '''Delete node'''
        if self.left and self.right:
            node = self.right.minimum()
            self.key = node.key
            node.delete()
        elif self.left:
            self.replace(self.left)
        elif self.right:
            self.replace(self.right)
        else:
            if self.parent is None:
                self.key = None
            elif self.parent.left is self:
                self.parent.left = None
            elif self.parent.right is self:
                self.parent.right = None
        

    def traverse(self, A=None):
        if A is None:
            A = []
        if self.left:
            self.left.traverse(A)
        A.append(self.key)
        if self.right:
            self.right.traverse(A)
        return A
    
class TestBST(unittest.TestCase):
    def test_01(self):
        bst = BST(5)
        x = bst.traverse()
        self.assertTrue(x == [5])

    def test_02(self):
        root = BST(2)
        root.insert(5)
        root.insert(1)
        root.insert(3)
        root.insert(4)
        x = root.traverse()
        self.assertTrue(x == [1, 2, 3, 4, 5])

    def test_03(self):
        root = BST(5)
        root.insert(2)
        root.delete()
        self.assertTrue(root.key == 2)

if __name__ == "__main__":
    res = unittest.main(verbosity = 3, exit = False)
