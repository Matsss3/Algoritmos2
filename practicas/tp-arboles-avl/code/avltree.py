from linkedlist import LinkedList, add

class AVLTree:
    def __init__(self):
        self.root: AVLNode|None = None

class AVLNode:
    def __init__(self, key = -1, value = None):
        self.parent: AVLNode|None = None
        self.leftnode: AVLNode|None = None
        self.rightnode: AVLNode|None = None
        self.key = key
        self.value = value
        self.bf: int = 0

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

def insertBT(B: AVLTree, e, k: int) -> int|None:
    newNode = AVLNode(k, e)

    if B.root == None:
        B.root = newNode
        return k

    return _insertBT(B.root, newNode)

def _insertBT(current: AVLNode, N: AVLNode) -> int|None:
    if current.key is not None:
        if current.key > N.key:
            if current.leftnode:
                return _insertBT(current.leftnode, N)
            else:
                current.leftnode = N
                N.parent = current
                return N.key
        elif current.key < N.key:
            if current.rightnode:
                return _insertBT(current.rightnode, N)
            else:
                current.rightnode = N
                N.parent = current
                return N.key
    else:
        return None

def traverseInOrder(A: AVLTree) -> LinkedList:
    result = LinkedList()
    _traverseInOrder(A.root, result)
    return result

def _traverseInOrder(N: AVLNode|None, L: LinkedList):
    if N:
        _traverseInOrder(N.rightnode, L)
        add(L, N)
        _traverseInOrder(N.leftnode, L)

def traverseInPostOrder(A: AVLTree) -> LinkedList:
    result = LinkedList()
    _traverseInPostOrder(A.root, result)
    return result

def _traverseInPostOrder(N: AVLNode|None, L: LinkedList):
    if N:
        add(L, N)
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
        add(L, N)

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
    parent = N.parent

    newRoot.leftnode = N
    N.rightnode = subTree
    if subTree:
        subTree.parent = N

    newRoot.parent = N.parent
    N.parent = newRoot

    if parent:
        if parent.leftnode == N:
            parent.leftnode = newRoot
        elif parent.rightnode == N:
            parent.rightnode = newRoot
    else:
        A.root = newRoot

    N.bf = height(N.leftnode) - height(N.rightnode)
    newRoot.bf = height(newRoot.leftnode) - height(newRoot.rightnode)

    return newRoot

def rotateRight(A: AVLTree, N: AVLNode|None) -> AVLNode|None:
    if N == None or N.leftnode == None:
        return None

    newRoot = N.leftnode
    subTree = newRoot.rightnode
    parent = N.parent

    newRoot.rightnode = N
    N.leftnode = subTree
    if subTree:
        subTree.parent = N

    newRoot.parent = N.parent
    N.parent = newRoot

    if parent:
        if parent.leftnode == N:
            parent.leftnode = newRoot
        elif parent.rightnode == N:
            parent.rightnode = newRoot
    else:
        A.root = newRoot

    N.bf = height(N.leftnode) - height(N.rightnode)
    newRoot.bf = height(newRoot.leftnode) - height(newRoot.rightnode)

    return newRoot

# ========== EJERCICIO 2 ==========
def calculateBalance(A: AVLTree) -> list[list]|None:
    if A.root == None:
        return None

    result = []
    nodeList = traverseInOrder(A)
    current = nodeList.head
    while current is not None:
        result.append([current.value, current.value.bf])
        current = current.nextNode
    return result

# ========== EJERCICIO 3 ==========
def rebalance(A: AVLTree, N: AVLNode|None) -> AVLNode|None:
    if N == None:
        return None

    N.leftnode = rebalance(A, N.leftnode)
    N.rightnode = rebalance(A, N.rightnode)
    N.bf = height(N.leftnode) - height(N.rightnode)

    leftNode_bf = N.leftnode.bf if N.leftnode else 0
    rightNode_bf = N.rightnode.bf if N.rightnode else 0

    # LL
    if N.bf > 1 and leftNode_bf >= 0:
        return rotateRight(A, N)
    #RR
    elif N.bf < -1 and rightNode_bf <= 0:
        return rotateLeft(A, N)
    #LR
    elif N.bf > 1 and leftNode_bf < 0:
        rotateLeft(A, N.leftnode)
        return rotateRight(A, N)
    #RL
    elif N.bf < -1 and rightNode_bf > 0:
        rotateRight(A, N.rightnode)
        return rotateLeft(A, N)

    return N

def reBalance(A: AVLTree) -> AVLTree|None:
    if A.root == None:
        return None

    A.root = rebalance(A, A.root)
    return A

# ========== EJERCICIO 4 ==========
def insert(A: AVLTree, e, k: int) -> AVLNode:
    newNode = AVLNode(k, e)

    if A.root == None:
        A.root = newNode
        return newNode

    A.root = _insert(A, A.root, newNode)
    return newNode

def _insert(A: AVLTree, current: AVLNode, N: AVLNode) -> AVLNode|None:
    if current.key is not None:
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
        leftNode_bf = current.leftnode.bf if current.leftnode else 0
        rightNode_bf = current.rightnode.bf if current.rightnode else 0
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
            rotateLeft(A, current.leftnode)
            rotation = rotateRight(A, current)
            current = rotation if rotation else current
        #RL
        elif current.bf < -1 and rightNode_bf > 0:
            rotateRight(A, current.rightnode)
            rotation = rotateLeft(A, current)
            current = rotation if rotation else current

        return current
    else:
        return None

# ========== EJERCICIO 5 ==========
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

def delete(A: AVLTree, k: int) -> int|None:
    if A.root == None:
        return None

    A.root = _delete(A, A.root, k)
    return k

def _delete(A: AVLTree, N: AVLNode|None, k: int) -> AVLNode|None:
    if N == None:
        return None

    if k < N.key:
        N.leftnode = _delete(A, N.leftnode, k)
    elif k > N.key:
        N.rightnode = _delete(A, N.rightnode, k)
    else:
        replacement = mayorIzq(N.leftnode)
        if replacement == None:
            replacement = menorDer(N.rightnode)
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
            replacement.parent = N.parent
            replacement.leftnode = N.leftnode
            replacement.rightnode = N.rightnode
            if N == A.root:
                A.root = replacement
            else:
                if N.parent:
                    if N.parent.rightnode == N:
                        N.parent.rightnode = replacement
                    elif N.parent.leftnode == N:
                        N.parent.leftnode = replacement
            N.parent = None
            N.rightnode = None
            N.leftnode = None
            return replacement
        else:
            if N == A.root:
                A.root = None
            else:
                if N.parent:
                    if N.parent.rightnode == N:
                        N.parent.rightnode = None
                    elif N.parent.leftnode == N:
                        N.parent.leftnode = None
                N.parent = None
                return replacement

    N.bf = height(N.leftnode) - height(N.rightnode)
    leftNode_bf = N.leftnode.bf if N.leftnode else 0
    rightNode_bf = N.rightnode.bf if N.rightnode else 0

    # LL
    if N.bf > 1 and leftNode_bf >= 0:
        rotation = rotateRight(A, N)
        N = rotation if rotation else N
    #RR
    elif N.bf < -1 and rightNode_bf <= 0:
        rotation = rotateLeft(A, N)
        N = rotation if rotation else N
    #LR
    elif N.bf > 1 and leftNode_bf < 0:
        rotateLeft(A, N.leftnode)
        rotation = rotateRight(A, N)
        N = rotation if rotation else N
    #RL
    elif N.bf < -1 and rightNode_bf > 0:
        rotateRight(A, N.rightnode)
        rotation = rotateLeft(A, N)
        N = rotation if rotation else N

    return N



def generate_test_tree():
    tree = AVLTree()
    keys = [
        6, 18, 31, 43, 56, 68, 81, 93,
        25, 50, 75,
        # 2, 9, 15, 21, 33, 40, 59, 65, 79, 90, 97,
        12, 37, 62, 87
    ]
    for key in keys:
        insert(tree, str(key), key)
        # insertBT(tree, str(key), key)
    return tree

if __name__ == '__main__':
    test_tree = generate_test_tree()
    print_avl(test_tree.root)

    traverseInOrder(test_tree).print_list()
    balanceList = calculateBalance(test_tree)
    if balanceList:
        print([(i[0].key, i[1]) for i in balanceList])

    print(delete(test_tree, 18))
    print(delete(test_tree, 6))
    print_avl(test_tree.root)

    # test_tree2 = generate_test_tree()
    # print_avl(test_tree2.root)
    # balanceList = []
    # nodeList = traverseInOrder(test_tree2)
    # current = nodeList.head
    # while current is not None:
    #     current.value.bf = height(current.value.leftnode) - height(current.value.rightnode)
    #     balanceList.append((current.value.key, current.value.bf))
    #     current = current.nextNode
    # print(balanceList)
    # # Hicieron falta dos pasadas, el arbol estaba muy desbalanceado
    # reBalance(test_tree2)
    # reBalance(test_tree2)
    #
    # print_avl(test_tree2.root)
    # finalBalance = calculateBalance(test_tree2)
    # if finalBalance:
    #     print([(i[0].key, i[1]) for i in finalBalance])
