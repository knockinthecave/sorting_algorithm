class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(temp.key, node.right)

        return node

    def _get_min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current
