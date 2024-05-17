class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursively(self.root, val)

    def _insert_recursively(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursively(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursively(node.right, val)

    def inorder_traversal(self, node):
        elements = []
        if node:
            elements += self.inorder_traversal(node.left)
            elements.append(node.val)
            elements += self.inorder_traversal(node.right)
        return elements

# Kullanıcıdan bir string girdisi al
arr_input = input("Lütfen bir string girin: ")

# Stringi liste haline getirme ve gereksiz karakterleri kaldırma
arr = [int(x) for x in arr_input.strip("[]").split(',')]

# BST oluşturma
bst = BST()
for num in arr:
    bst.insert(num)

# BST'nin inorder traversal ile içeriğini yazdırma
sorted_elements = bst.inorder_traversal(bst.root)
print("Inorder Traversal:", sorted_elements)