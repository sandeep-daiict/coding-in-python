from collections import deque
class TreeNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        self.count_left = 0
        self.count_right = 0

    def __repr__(self):
        return "<value: " + str(self.data) + " left_count:"+str(self.count_left) + " right_count:"+str(self.count_right)+">"


class BST(object):
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, node, value):
        if node.data > value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_node(node.left, value)
            node.count_left = node.count_left + 1
        if node.data < value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert_node(node.right, value)
            node.count_right= node.count_right+ 1

    def height(self):
        return self.height_recur(self.root)

    def height_recur(self, node):
        if node is None:
            return 0
        return 1 + max(self.height_recur(node.left), self.height_recur(node.right))


    def __repr__(self):
        s = ""
        for d in range(1, self.height()+1):
            s = s + self.get_given_level(self.root, d)
            s = s + "\n"
        return s

    def get_given_level(self, node, level):
        if level==1:
            return str(node)
        l = ""
        r = ""
        if node.left is not None:
            l = self.get_given_level(node.left, level-1)
        if node.right is not None:
            r = self.get_given_level(node.right, level-1)
        return l + r

n = int(raw_input())
arr = [int(a) for a in raw_input().strip().split(" ")]
bt = BST()
for a in arr:
    bt.insert(a)
print(bt)
