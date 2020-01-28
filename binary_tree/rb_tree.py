class Node:
    def __init__(self, key):
        self.left = self.right=None
        self.key = key
        self.isRed = True

    def __str__(self):
        return f'key={self.key}, isRed={self.isRed}'

    def __repr__(self):
        return f'key={self.key}, isRed={self.isRed}'

class RBT:
    def __init__(self):
        self.root = None
    
    def insert(self, root, node):
        if not root:
            return node
        elif node.key == root.key:
            pass
        elif node.key < root.key:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)

        if root.right and root.right.isRed:
            root = self.left_rotate(root)
        if root.left and root.left.isRed and root.left.left and root.left.left.isRed:
            root = self.right_rotate(root)
        if root.left and root.left.isRed and root.right and root.right.isRed:
            root = self.flip_colors(root)
        return root

    def left_rotate(self, root):
        assert root.right
        assert root.right.isRed
        root.isRed, root.right.isRed = root.right.isRed, root.isRed
        tmp = root.right
        root.right = tmp.left
        tmp.left = root
        return tmp

    def right_rotate(self, root):
        assert root.left.isRed
        assert root.left.left.isRed
        root.left.isRed, root.isRed = root.isRed, root.left.isRed
        tmp = root.left
        root.left = tmp.right
        tmp.right = root
        return tmp

    def flip_colors(self, root):
        assert root.left
        assert root.right
        assert root.left.isRed
        assert root.right.isRed
        root.left.isRed = root.left.isRed = False
        root.isRed = True
        return root


    def inorder(self, root, data=None):
        if root:
            self.inorder(root.left, data)
            data.append(root.key)
            self.inorder(root.right, data)
    
    def get_min(self, root):
        while(root and root.left):
            root = root.left
        return root

    def delete(self, root, key):
        #import pdb; pdb.set_trace()
        if root:
            if key < root.key:
                root.left = self.delete(root.left, key) 
            elif key > root.key:
                root.right = self.delete(root.right, key)
            else:
                if not root.right:
                    root = root.left
                else:
                    tmp = self.get_min(root.right)
                    root.key = tmp.key
                    root.right = self.delete(root.right, tmp.key)

            if root and root.right and root.right.isRed:
                root = self.left_rotate(root)
            if root and root.left and root.left.isRed and root.left.left and root.left.left.isRed:
                root = self.right_rotate(root)
            if root and root.left and root.left.isRed and root.right and root.right.isRed:
                root = self.flip_colors(root)
        return root

import unittest
import random
class TestRBTree(unittest.TestCase):
    def setUp(self):
        self.size = 100
        self.items = list(set([random.randint(1,self.size*self.size) for x in range(self.size)]))
        #self.items = [12, 9, 8, 13]
        #self.items = [64, 7, 99, 95, 60]

    def test_RBTSort(self):
        rbt = RBT()
        for each in self.items:
            rbt.root = rbt.insert(rbt.root, Node(each))
            rbt.root.isRed = False
            tmp = []
            rbt.inorder(rbt.root, tmp)
        tmp = []
        rbt.inorder(rbt.root, tmp)
        print(self.items)
        assert tmp==sorted(self.items)

    def test_delete_RBTSort(self):
        rbt = RBT()
        for each in self.items:
            rbt.root = rbt.insert(rbt.root, Node(each))
            rbt.root.isRed = False
            tmp = []
            rbt.inorder(rbt.root, tmp)
        to_del = random.sample(self.items, len(self.items)//4)
        for each in to_del:
            rbt.root = rbt.delete(rbt.root, each)
            self.items.remove(each)
        tmp = []
        rbt.inorder(rbt.root, tmp)
        print(self.items)
        assert tmp==sorted(self.items)

if __name__ == '__main__':
    unittest.main()
