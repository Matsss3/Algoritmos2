from typing import Any, cast
import copy

from dictionary import *
from myqueue import *

class Graph:
    def __init__(self, v: lk.LinkedList, e: lk.LinkedList) -> None:
        self.v = v
        self.e = e
        self.graph = self.createGraph()

    # Ejercicio 1
    def createGraph(self) -> Dictionary:
        v = self.v
        e = self.e

        graph = Dictionary(lk.length(v))
        curr_v = v.head
        while curr_v is not None:
            insert(graph, curr_v.value)
            curr_v = curr_v.nextNode

        curr_e = e.head
        while curr_e is not None:
            v_i, v_j = cast(tuple[Any, Any], curr_e.value)

            if search(graph, v_i) is None or search(graph, v_j) is None:
                continue
            
            insert(graph, v_j, key = graph.hash_func(v_i))
            insert(graph, v_i, key = graph.hash_func(v_j))
            curr_e = curr_e.nextNode

        return graph

    def printGraph(self) -> None:
        d = self.graph
        for i in range(d.m):
            print(f"[{i}]", end=" ")
            d.dictionary[i].print_list()


# Ejercicio 2
def existPath(G: Graph, v1: Any, v2: Any) -> bool:
    if search(G.graph, v1) is None or search(G.graph, v2) is None:
        return False

    visited = [v1]
    Q = lk.LinkedList()
    enqueue(Q, v1)

    while Q.head is not None:
        u = dequeue(Q)
        curr_e = G.graph.dictionary[G.graph.hash_func(u)].head
        while curr_e is not None:
            v = curr_e.value[1]
            if v not in visited:
                if v == v2:
                    return True
                enqueue(Q, v)
                visited.append(v)
            curr_e = curr_e.nextNode

    return False

# Ejercicio 3
def isConnected(G: Graph) -> bool:
    v = G.v 
    visited = []

    def dfs_visit(G: Graph, u):
        visited.append(u)
        adj_u = G.graph.dictionary[G.graph.hash_func(u)].head
        while adj_u is not None:
            v = adj_u.value[1]
            if v not in visited:
                dfs_visit(G, v)
            adj_u = adj_u.nextNode

    if v.head is not None:
        dfs_visit(G, v.head.value)
        if len(visited) == lk.length(v):
            return True
        else:
            return False
    return True

# Ejercicio 4
def isTree(G: Graph) -> bool:
    is_conn = isConnected(G)
    if is_conn and lk.length(G.e) == (lk.length(G.v) - 1):
        return True
    return False

# Ejercicio 5
def isComplete(G: Graph) -> bool:
    v = lk.length(G.v)
    if lk.length(G.e) == (v * (v-1)) // 2:
        return True
    else:
        return False

# Ejercicio 6
def BFS(G: Graph, s) -> list[tuple[Any, Any]]:
    visited = [s]
    result = []

    Q = lk.LinkedList()
    enqueue(Q, s)
    while Q.head is not None:
        u = dequeue(Q)
        curr_e = G.graph.dictionary[G.graph.hash_func(u)].head
        while curr_e is not None:
            v = curr_e.value[1]
            if v not in visited:
                visited.append(v)
                enqueue(Q, v)
                result.append((u, v))
            curr_e = curr_e.nextNode

    return result

def convertTree(G: Graph) -> lk.LinkedList:
    result = lk.LinkedList()
    e = G.e
    curr_e = e.head
    while curr_e is not None:
        u, v = cast(tuple[Any, Any], curr_e.value)
        graph = copy.deepcopy(G)
        # graph.printGraph()
        delete(graph.graph, G.graph.hash_func(u), v)

        if isConnected(graph):
            lk.add(result, curr_e.value)

        curr_e = curr_e.nextNode
    return result


# ========== TESTING ==========
def build_list(values) -> lk.LinkedList:
    lst = lk.LinkedList()
    for value in values:
        lk.add(lst, value)
    return lst

def test_int_graph() -> Graph:
    print("--- integer graph ---")
    v = build_list([1, 2, 3, 4, 5])
    e = build_list([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
    graph = Graph(v, e)
    graph.printGraph()
    return graph
 
def test_str_graph() -> Graph:
    print("--- string graph ---")
    v = build_list(["A", "B", "C", "D"])
    e = build_list([("A", "B"), ("A", "C"), ("B", "C")])
    graph = Graph(v, e)
    graph.printGraph()
    return graph
 
if __name__ == "__main__":
    graph1 = test_int_graph()
    graph2 = test_str_graph()
    print()

    # print(existPath(graph1, 1, 4))
    # print()
    #
    # print(isConnected(graph1))
    # print(isConnected(graph2))
    # print()

    # print(isTree(graph1))

    # convertTree(graph1).print_list()
