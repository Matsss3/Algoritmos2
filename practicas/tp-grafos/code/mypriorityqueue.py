class PriorityQueue:
    head = None

class PriorityNode:
    value = None
    nextNode = None
    priority = None

def print_list(lista):
    end_str = "[\n"
    currentNode = lista.head
    while currentNode != None:
        end_str += f"value:{currentNode.value}, pr:{currentNode.priority}\n"
        currentNode = currentNode.nextNode
    end_str += "]"
    print(end_str)

# ========== EJERCICIO 3 ==========

def enqueue_priority(Q, element, priority):
    newNode = PriorityNode()
    newNode.value = element
    newNode.priority = priority
    currentNode = Q.head

    if currentNode == None or priority > currentNode.priority:
        newNode.nextNode = Q.head
        Q.head = newNode
        return 0

    counter = 0
    while currentNode.nextNode != None and currentNode.nextNode.priority >= priority:
        currentNode = currentNode.nextNode
        counter += 1

    newNode.nextNode = currentNode.nextNode
    currentNode.nextNode = newNode
    return counter

def dequeue_priority(Q):
    element = Q.head
    if element != None and Q.head.nextNode != None:
        Q.head = Q.head.nextNode
    else:
        Q.head = None
    return element.value if element != None else None
