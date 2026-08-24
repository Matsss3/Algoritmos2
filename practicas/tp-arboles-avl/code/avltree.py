from linkedlist import LinkedList, add

class AVLTree:
    def __init__(self):
        self.root: AVLNode|None = None

class AVLNode:
    def __init__(self, key = None, value = None):
        self.parent: AVLNode|None = None
        self.leftnode: AVLNode|None = None
        self.rightnode: AVLNode|None = None
        self.key = key
        self.value = value
        self.bf: int|None = None

def searchNode(N: AVLNode|None, e) -> AVLNode|None:
    if N == None:
        return None
    if N.value == e:
        return N
    current = searchNode(N.leftnode, e)
    if current == None:
        return searchNode(N.rightnode, e)
    else:
        return current

def mayorIzq(N: AVLNode|None) -> AVLNode|None:
    if N:
        if N.rightnode:
            return mayorIzq(N.rightnode)
        return N

def menorDer(N: AVLNode|None) -> AVLNode|None:
    if N:
        if N.leftnode:
            return menorDer(N.leftnode)
        return N

def delete(A: AVLTree, e) -> int|None:
    node = searchNode(A.root, e)
    if node == None:
        return None
    replacement = mayorIzq(node.leftnode)
    if replacement == None:
        replacement = menorDer(node.rightnode)
    if replacement and replacement.parent:
        if replacement.leftnode:
            replacement.parent.rightnode = replacement.leftnode
            replacement.leftnode.parent = replacement.parent
        elif replacement.rightnode:
            replacement.parent.leftnode = replacement.rightnode
            replacement.rightnode.parent = replacement.parent
        else:
            if replacement.parent.rightnode == replacement:
                replacement.parent.rightnode = None
            elif replacement.parent.leftnode == replacement:
                replacement.parent.leftnode = None
        replacement.parent = node.parent
        replacement.leftnode = node.leftnode
        replacement.rightnode = node.rightnode
        if node == A.root:
            A.root = replacement
        else:
            if node.parent:
                if node.parent.rightnode == node:
                    node.parent.rightnode = replacement
                elif node.parent.leftnode == node:
                    node.parent.leftnode = replacement
        node.parent = None
        node.rightnode = None
        node.leftnode = None
        return node.key
    else:
        if node == A.root:
            A.root = None
        else:
            if node.parent:
                if node.parent.rightnode == node:
                    node.parent.rightnode = None
                elif node.parent.leftnode == node:
                    node.parent.leftnode = None
            node.parent = None
            return node.key
    return None

def traverseInOrder(A: AVLTree) -> LinkedList:
    result = LinkedList()
    _traverseInOrder(A.root, result)
    return result

def _traverseInOrder(N: AVLNode|None, L: LinkedList):
    if N:
        _traverseInOrder(N.rightnode, L)
        add(L, N.key)
        _traverseInOrder(N.leftnode, L)

def traverseInPostOrder(A: AVLTree) -> LinkedList:
    result = LinkedList()
    _traverseInPostOrder(A.root, result)
    return result

def _traverseInPostOrder(N: AVLNode|None, L: LinkedList):
    if N:
        add(L, N.key)
        _traverseInPostOrder(N.rightnode, L)
        _traverseInPostOrder(N.leftnode,L)

def traverseInPreOrder(A: AVLTree) -> LinkedList:
    result = LinkedList()
    _traverseInPreOrder(A.root, result)
    return result

def _traverseInPreOrder(N: AVLNode|None, L: LinkedList):
    if N:
        _traverseInPreOrder(N.rightnode, L)
        _traverseInPreOrder(N.leftnode,L)
        add(L, N.key)

# O(logn) porque siempre verifica el factor de balanceo para ir por una sola rama
# del árbol en cada paso, efectivamente dividiendolo en 2 en cada paso (a menos
# que el balance factor no exista).
def height(N: AVLNode|None) -> int:
    if N == None:
        return 0

    if N.bf:
        if N.bf > 0:
            return 1 + height(N.leftnode)
        else:
            return 1 + height(N.rightnode)

    return 1 + max(height(N.leftnode), height(N.rightnode))

def print_avl(N: AVLNode|None, space=0, count=5):
    if N == None:
        return
    
    space += count
    print_avl(N.rightnode, space, count)
    
    print()
    for i in range(count, space):
        print(end=" ")
    print(N.key)
    
    print_avl(N.leftnode, space, count)

# ========== EJERCICIO 1 ==========
def rotateLeft(A: AVLTree, N: AVLNode|None) -> AVLNode|None:
    if N == None or N.rightnode == None:
        return None

    newRoot = N.rightnode
    subTree = newRoot.leftnode

    newRoot.leftnode = N
    N.rightnode = subTree
    if subTree:
        subTree.parent = N

    newRoot.parent = N.parent
    N.parent = newRoot

    N.bf = height(N.leftnode) - height(N.rightnode)
    newRoot.bf = height(newRoot.leftnode) - height(newRoot.rightnode)

    if A.root == N:
        A.root = newRoot

    return newRoot

def rotateRight(A: AVLTree, N: AVLNode|None) -> AVLNode|None:
    if N == None or N.leftnode == None:
        return None

    newRoot = N.leftnode
    subTree = newRoot.rightnode

    newRoot.rightnode = N
    N.leftnode = subTree
    if subTree:
        subTree.parent = N

    newRoot.parent = N.parent
    N.parent = newRoot

    N.bf = height(N.leftnode) - height(N.rightnode)
    newRoot.bf = height(newRoot.leftnode) - height(newRoot.rightnode)

    if A.root == N:
        A.root = newRoot

    return newRoot

# ========== EJERCICIO 3 ==========
def insert(A: AVLTree, e, k: int) -> AVLNode:
    newNode = AVLNode(k, e)

    if A.root == None:
        A.root = newNode
        return newNode

    A.root = _insert(A, A.root, newNode)
    return newNode

def _insert(A: AVLTree, current: AVLNode, N: AVLNode) -> AVLNode|None:
    if current.key:
        if current.key > N.key:
            if current.leftnode:
                current.leftnode = _insert(A, current.leftnode, N)
            else:
                current.leftnode = N
                N.parent = current
        elif current.key < N.key:
            if current.rightnode:
                current.rightnode = _insert(A, current.rightnode, N)
            else:
                current.rightnode = N
                N.parent = current
        else:
            return current

        current.bf = height(current.leftnode) - height(current.rightnode)
        leftNode_bf = current.leftnode.bf if current.leftnode and current.leftnode.bf else 0
        rightNode_bf = current.rightnode.bf if current.rightnode and current.rightnode.bf else 0
        # LL
        if current.bf > 1 and leftNode_bf >= 0:
            rotation = rotateRight(A, current)
            current = rotation if rotation else current
        #RR
        elif current.bf < -1 and rightNode_bf <= 0:
            rotation = rotateLeft(A, current)
            current = rotation if rotation else current
        #LR
        elif current.bf > 1 and leftNode_bf < 0:
            current.leftnode = rotateLeft(A, current.leftnode)
            rotation = rotateRight(A, current)
            current = rotation if rotation else current
        #RL
        elif current.bf < -1 and rightNode_bf > 0:
            current.rightnode = rotateRight(A, current.rightnode)
            rotation = rotateLeft(A, current)
            current = rotation if rotation else current

        return current
    else:
        return None




def generate_test_tree():
    tree = AVLTree()
    keys = [
        6, 18, 31, 43, 56, 68, 81, 93,
        25, 50, 75,
        2, 9, 15, 21, 33, 40, 59, 65, 79, 90, 97,
        12, 37, 62, 87
    ]
    for key in keys:
        insert(tree, str(key), key)
    return tree

test_tree = generate_test_tree()
print_avl(test_tree.root)

traverseInOrder(test_tree).print_list()
