from linkedlist import LinkedList, add
from myqueue import enqueue, dequeue
from mystack import push, pop

class BinaryTree:
    def __init__(self):
        self.root = None

class BinaryTreeNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.leftnode = None
        self.rightnode = None
        self.parent = None

# def generate_test_tree():
#     tree = BinaryTree()
#     keys = [
#         50, 25, 75,
#         12, 37, 62, 87,
#         6, 18, 31, 43, 56, 68, 81, 93,
#         2, 9, 15, 21, 33, 40, 59, 65, 79, 90, 97
#     ]
#     for key in keys:
#         insert(tree, str(key), key)
#     return tree

def searchNode(N: BinaryTreeNode, e) -> BinaryTreeNode|None:
    if N == None:
        return None
    if N.value == e:
        return N
    current = searchNode(N.leftnode, e)
    if current == None:
        return searchNode(N.rightnode, e)
    else:
        return current

# ========== EJERCICIO 1 ===========
def search(B: BinaryTree, e) -> int|None:
    tree = traverseInOrder(B)
    current = tree.head
    while current != None:
        if current.value.value == e:
            return current.value.key
        current = current.nextNode
    return None

def insert(B: BinaryTree, e, k: int) -> int|None:
    newNode = BinaryTreeNode(k, e)

    if B.root == None:
        B.root = newNode
        return k

    return _insert(B.root, newNode)

def _insert(current: BinaryTreeNode, N: BinaryTreeNode) -> int|None:
    if current.key > N.key:
        if current.leftnode:
            return _insert(current.leftnode, N)
        else:
            current.leftnode = N
            N.parent = current
            return N.key
    elif current.key < N.key:
        if current.rightnode:
            return _insert(current.rightnode, N)
        else:
            current.rightnode = N
            N.parent = current
            return N.key
    else:
        return None

def delete(B: BinaryTree, e) -> int|None:
    node = searchNode(B.root, e)
    if node == None:
        return None
    replacement = mayorIzq(node.leftnode)
    if replacement == None:
        replacement = menorDer(node.rightnode)
    if replacement:
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
        if node == B.root:
            B.root = replacement
        else:
            if node.parent.rightnode == node:
                node.parent.rightnode = replacement
            elif node.parent.leftnode == node:
                node.parent.leftnode = replacement
        node.parent = None
        node.rightnode = None
        node.leftnode = None
        return node.key
    else:
        if node == B.root:
            B.root = None
        else:
            if node.parent.rightnode == node:
                node.parent.rightnode = None
            elif node.parent.leftnode == node:
                node.parent.leftnode = None
            node.parent = None
            return node.key
    return None

def deleteKey(B: BinaryTree, k: int) -> int|None:
    element = access(B, k)
    return delete(B, element)

def mayorIzq(N: BinaryTreeNode|None) -> BinaryTreeNode|None:
    if N:
        if N.rightnode:
            return mayorIzq(N.rightnode)
        return N

def menorDer(N: BinaryTreeNode|None) -> BinaryTreeNode|None:
    if N:
        if N.leftnode:
            return menorDer(N.leftnode)
        return N

def access(B: BinaryTree, key: int):
    return _access(B.root, key)

def _access(N: BinaryTreeNode, key: int):
    if N:
        if N.key > key:
            return _access(N.leftnode, key)
        elif N.key < key:
            return _access(N.rightnode, key)
        else:
            return N.value
    else:
        return None

def update(B: BinaryTree, element, key: int) -> int|None:
    return _update(B.root, element, key)

def _update(N: BinaryTreeNode, element, key: int) -> int|None:
    if N:
        if N.key > key:
            return _update(N.leftnode, element, key)
        elif N.key < key:
            return _update(N.rightnode, element, key)
        else:
            N.value = element
            return key
    else:
        return None

# ========== EJERCICIO 2 ===========
def traverseInOrder(B: BinaryTree) -> LinkedList:
    result = LinkedList()
    _traverseInOrder(B.root, result)
    return result

def _traverseInOrder(N: BinaryTreeNode, L: LinkedList):
    if N:
        _traverseInOrder(N.rightnode, L)
        add(L, N)
        _traverseInOrder(N.leftnode, L)

def traverseInPostOrder(B: BinaryTree) -> LinkedList:
    result = LinkedList()
    _traverseInPostOrder(B.root, result)
    return result

def _traverseInPostOrder(N: BinaryTreeNode, L: LinkedList):
    if N:
        add(L, N)
        _traverseInPostOrder(N.rightnode, L)
        _traverseInPostOrder(N.leftnode,L)

def traverseInPreOrder(B: BinaryTree) -> LinkedList:
    result = LinkedList()
    _traverseInPreOrder(B.root, result)
    return result

def _traverseInPreOrder(N: BinaryTreeNode, L: LinkedList):
    if N:
        _traverseInPreOrder(N.rightnode, L)
        _traverseInPreOrder(N.leftnode,L)
        add(L, N)

def traverseBreadFirst(B: BinaryTree) -> LinkedList:
    aux = LinkedList()
    result = LinkedList()
    queue = LinkedList()
    enqueue(queue, B.root)
    current = B.root
    while current:
        current = dequeue(queue)
        if current:
            push(aux, current)
            if current.leftnode:
                enqueue(queue, current.leftnode)
            if current.rightnode:
                enqueue(queue, current.rightnode)
    while aux.head:
        add(result, pop(aux))
    return result
#
# tree = generate_test_tree()
#
# result = traverseInOrder(tree)
#
# print("Traverse In Order:")
#
# current = result.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
#
# result2 = traverseInPostOrder(tree)
#
# print("Traverse In Post Order:")
#
# current = result2.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
#
# result3 = traverseInPreOrder(tree)
#
# print("Traverse In Pre Order:")
#
# current = result3.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
#
# result4 = traverseBreadFirst(tree)
#
# print("Traverse Bread First:")
#
# current = result4.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
#
# print("Search for 15:")
# print(search(tree, "15"))
#
# print("Insert 24:")
# print(insert(tree, "24", 24))
# result5 = traverseInOrder(tree)
# current = result5.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
#
# print("Access 43:")
# print(access(tree, 43))
#
# print("Update 75 -> 74:")
# print(update(tree, "74", 75))
# result6 = traverseInOrder(tree)
# current = result6.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
#
# print("Delete 18:")
# print(deleteKey(tree, 18))
# result7 = traverseBreadFirst(tree)
# current = result7.head
# while current is not None:
#     print(current.value.value, end=" ")
#     current = current.nextNode
# print("")
