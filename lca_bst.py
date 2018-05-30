
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        a,b = list(map(int, input().strip().split()))
        res = LCA(root, a, b)
        print(res.data)
# Contributed by: Harshit Sidhwa
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# function should return the required lca node
def LCA(root, a, b):
    if root is None:
        return root
    if root.data == a or root.data == b:
        return root;
    # Code here
    x = min(a,b)
    y = max(a,b)
    if(root.data > x and root.data < y):
        return root
    if(root.left is not None):
        left_lca = LCA(root.left, x, y)
        if left_lca is not None:
            return left_lca
    if(root.right is not None):
        right_lca = LCA(root.right, x, y)
        if right_lca is not None:
            return right_lca
    return None
