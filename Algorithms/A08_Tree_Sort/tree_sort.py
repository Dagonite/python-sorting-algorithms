# tree_sort.py
"""
Worst complexity:   n ** 2 (unbalanced) / n * log(n) (balanced)
Average complexity: n * log(n)
Best complexity:    n * log(n)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)

    def delete_tree(self):
        # garbage collector will do this for us.
        self.root = None

    def __str__(self):
        inorder = []
        self.print_inorder(self.root, inorder)
        return str(inorder)

    def print_inorder(self, node, inorder):
        if node is not None:
            self.print_inorder(node.left, inorder)
            inorder.append(node.val)
            self.print_inorder(node.right, inorder)


def tree_sort(items):
    tree = Tree()
    for i in items:
        tree.add(i)


if __name__ == "__main__":
    import time, random

    items = [random.randint(1, 1000) for _ in range(5000)]
    start = time.perf_counter()
    tree_sort(items)
    print(time.perf_counter() - start)