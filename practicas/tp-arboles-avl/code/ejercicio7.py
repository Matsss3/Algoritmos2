from avltree import * 
import unittest

def join_avl(A: AVLTree, x: int, B: AVLTree) -> AVLTree:
    if A.root == None and B.root == None:
        tree = AVLTree()
        insert(tree, str(x), x)
        return tree
    elif A.root == None and B.root is not None:
        insert(A, str(x), x)
        return A
    elif B.root == None and A.root is not None:
        insert(B, str(x), x)
        return B

    heightA = height(A.root)
    heightB = height(B.root)

    if abs(heightA - heightB) < 2:
        tree = AVLTree()
        insert(tree, str(x), x)
        if tree.root:
            tree.root.leftnode = A.root
            tree.root.rightnode = B.root
        return tree

    newNode = AVLNode(x, str(x))

    if heightA > heightB:
        node = A.root
        counter = heightA - heightB - 2

        while counter > 0 and node is not None:
            node = node.rightnode
            counter -= 1

        if node == None:
            return A

        rightNode = node.rightnode
        node.rightnode = newNode
        newNode.parent = node
        
        newNode.leftnode = rightNode
        if rightNode is not None:
            rightNode.parent = newNode
        
        newNode.rightnode = B.root
        return A
    else:
        node = B.root
        counter = heightB - heightA - 2

        while counter > 0 and node is not None:
            node = node.leftnode
            counter -= 1

        if node == None:
            return B

        leftNode = node.leftnode
        node.leftnode = newNode
        newNode.parent = node
        
        newNode.rightnode = leftNode
        if leftNode is not None:
            leftNode.parent = newNode
        
        newNode.leftnode = A.root
        return B


class TestJoinAVL(unittest.TestCase):

    def make_tree(self, keys):
        tree = AVLTree()

        for key in keys:
            insert(tree, str(key), key)

        return tree

    def get_height(self, node):
        if node is None:
            return 0

        return 1 + max(
            self.get_height(node.leftnode),
            self.get_height(node.rightnode)
        )

    def is_bst(self, node, minimum=None, maximum=None):
        if node is None:
            return True

        if minimum is not None and node.key <= minimum:
            return False

        if maximum is not None and node.key >= maximum:
            return False

        return (
            self.is_bst(node.leftnode, minimum, node.key)
            and
            self.is_bst(node.rightnode, node.key, maximum)
        )

    def is_avl(self, node):
        if node is None:
            return True

        left_height = self.get_height(node.leftnode)
        right_height = self.get_height(node.rightnode)

        if abs(left_height - right_height) > 1:
            return False

        return (
            self.is_avl(node.leftnode)
            and
            self.is_avl(node.rightnode)
        )

    def get_keys(self, node):
        if node is None:
            return []

        return (
            self.get_keys(node.leftnode)
            + [node.key]
            + self.get_keys(node.rightnode)
        )

    def assert_valid_avl(self, tree, expected_keys):
        self.assertIsNotNone(tree.root)

        self.assertTrue(
            self.is_bst(tree.root),
            "El resultado no es un BST"
        )

        self.assertTrue(
            self.is_avl(tree.root),
            "El resultado no es un árbol AVL válido"
        )

        actual_keys = self.get_keys(tree.root)

        self.assertEqual(
            actual_keys,
            sorted(expected_keys)
        )

    # ---------------------------------------------------------
    # TEST 1
    # Ambos árboles tienen un nodo
    # ---------------------------------------------------------

    def test_single_nodes(self):
        A = self.make_tree([2])
        B = self.make_tree([8])

        result = join_avl(A, 5, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            [2, 5, 8]
        )

    # ---------------------------------------------------------
    # TEST 2
    # Misma altura
    # ---------------------------------------------------------

    def test_same_height(self):
        A = self.make_tree([2, 4, 6])
        B = self.make_tree([12, 15, 18])

        result = join_avl(A, 10, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            [2, 4, 6, 10, 12, 15, 18]
        )

    # ---------------------------------------------------------
    # TEST 3
    # A es un poco más alto que B
    # ---------------------------------------------------------

    def test_a_slightly_taller(self):
        A = self.make_tree([2, 5, 7, 10, 15])
        B = self.make_tree([22, 25, 30])

        result = join_avl(A, 20, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            [2, 5, 7, 10, 15, 20, 22, 25, 30]
        )

    # ---------------------------------------------------------
    # TEST 4
    # A es mucho más alto que B
    # ---------------------------------------------------------

    def test_a_much_taller(self):
        A = self.make_tree([2, 5, 10, 15, 20, 30])
        B = self.make_tree([50])

        result = join_avl(A, 40, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            [2, 5, 10, 15, 20, 30, 40, 50]
        )

    # ---------------------------------------------------------
    # TEST 5
    # B es mucho más alto que A
    # ---------------------------------------------------------

    def test_b_much_taller(self):
        A = self.make_tree([10])

        B = self.make_tree([
            30, 40, 45, 50, 60, 70
        ])

        result = join_avl(A, 20, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            [10, 20, 30, 40, 45, 50, 60, 70]
        )

    # ---------------------------------------------------------
    # TEST 6
    # Ambos árboles tienen multiples nodos
    # ---------------------------------------------------------

    def test_multiple_nodes(self):
        A = self.make_tree([
            10, 20, 30, 40, 50, 60, 70
        ])

        B = self.make_tree([
            120, 130, 140, 150, 160, 170, 180
        ])

        result = join_avl(A, 100, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            [
                10, 20, 30, 40, 50, 60, 70,
                100,
                120, 130, 140, 150, 160, 170, 180
            ]
        )

    # ---------------------------------------------------------
    # TEST 7
    # A tiene muchos mas nodos que B
    # ---------------------------------------------------------

    def test_a_much_larger(self):
        A_keys = list(range(1, 16))
        B_keys = [100]

        A = self.make_tree(A_keys)
        B = self.make_tree(B_keys)

        result = join_avl(A, 50, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            A_keys + [50] + B_keys
        )

    # ---------------------------------------------------------
    # TEST 8
    # B tiene muchos mas nodos que A
    # ---------------------------------------------------------

    def test_b_much_larger(self):
        A_keys = [1]
        B_keys = list(range(100, 115))

        A = self.make_tree(A_keys)
        B = self.make_tree(B_keys)

        result = join_avl(A, 50, B)
        print_avl(result.root)
        print("="*10)

        self.assert_valid_avl(
            result,
            A_keys + [50] + B_keys
        )


if __name__ == "__main__":
    unittest.main()
