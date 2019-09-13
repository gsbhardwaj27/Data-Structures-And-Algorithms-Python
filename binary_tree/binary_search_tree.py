from random import randint, sample
import unittest


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.insertR(self.root, Node(key, value))

    def insertR(self, root, node):
        if not root:
            return node
        else:
            if node.key < root.key:
                root.left = self.insertR(root.left, node)
            elif node.key > root.key:
                root.right = self.insertR(root.right, node)
            else:
                root.value = node.value
            return root

    def present(self, root, key):
        if not root:
            return False
        else:
            if key < root.key:
                return self.present(root.left, key)
            elif key > root.key:
                return self.present(root.right, key)
            else:
                return True

    def getMin(self, root):
        if root:
            while root.left:
                root = root.left
        return root

    def delete(self, key):
        self.root = self.deleteR(self.root, key)

    def deleteR(self, root,  key):
        # breakpoint()
        if root:
            if key < root.key:
                root.left = self.deleteR(root.left, key)
            elif key > root.key:
                root.right = self.deleteR(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    next_min = self.getMin(root.right)
                    root.key = next_min.key
                    root.value = next_min.value
                    root.right = self.deleteR(root.right, next_min.key)
        return root

    def inorder(self):
        keys = []
        self.inorderR(self.root, keys)
        return keys

    def inorderR(self, root, keys):
        if root:
            self.inorderR(root.left, keys)
            keys.append(root.value)
            self.inorderR(root.right, keys)


class TestBST(unittest.TestCase):
    def setUp(self):
        self.mxval = 100000
        self.numnodes = 100
        self.values = [randint(0, self.mxval) for x in range(self.numnodes)]
        self.values = list(set(self.values))
        self.tree = BinarySearchTree()

    def test_1_empty(self):
        self.assertListEqual([], self.tree.inorder())

    def test_2_insert(self):
        for each in self.values:
            # For simplicity we will keep key and values
            # as same
            self.tree.insert(each, each)
        self.assertEqual(sorted(self.values), self.tree.inorder())

    def test_3_delete(self):
        for each in self.values:
            self.tree.insert(each, each)

        todelete = sample(self.values, self.numnodes//5)
        remainig_items = [x for x in self.values if x not in set(todelete)]
        for each in todelete:
            self.tree.delete(each)
        self.assertListEqual(sorted(remainig_items), self.tree.inorder())


if __name__ == '__main__':
    unittest.main()
