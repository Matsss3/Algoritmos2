from math import inf

from graph import *


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
            if isinstance(curr_e.value, tuple):
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
            if isinstance(adj_u.value, tuple):
                v = adj_u.value[1]
                if v not in visited:
                    dfs_visit(G, v)
            adj_u = adj_u.nextNode

    if v.head is not None:
        dfs_visit(G, v.head.value)
        if len(visited) == G.graph.m:
            return True
        else:
            return False
    return True

# Ejercicio 4
def isTree(G: Graph) -> bool:
    is_conn = isConnected(G)
    if is_conn and lk.length(G.e) == (G.graph.m - 1):
        return True
    return False

# Ejercicio 5
def isComplete(G: Graph) -> bool:
    v = G.graph.m
    if lk.length(G.e) == (v * (v-1)) // 2:
        return True
    else:
        return False

# Ejercicio 6
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

# Ejercicio 7
def countConnections(G: Graph) -> int:
    v = G.v.head
    visited = []
    result = 0

    def dfs_visit(G: Graph, u):
        visited.append(u)
        adj_u = G.graph.dictionary[G.graph.hash_func(u)].head
        while adj_u is not None:
            if isinstance(adj_u.value, tuple):
                v = adj_u.value[1]
                if v not in visited:
                    dfs_visit(G, v)
            adj_u = adj_u.nextNode

    while v is not None:
        if v.value not in visited:
            dfs_visit(G, v.value)
            result += 1
        v = v.nextNode

    return result

# Ejercicio 8
def BFS(G: Graph, s) -> Graph:
    if not isConnected(G):
        return G

    visited = [s]
    new_e = lk.LinkedList()

    Q = lk.LinkedList()
    enqueue(Q, s)
    while Q.head is not None:
        u = dequeue(Q)
        curr_e = G.graph.dictionary[G.graph.hash_func(u)].head
        while curr_e is not None:
            if isinstance(curr_e.value, tuple):
                v = curr_e.value[1]
                if v not in visited:
                    visited.append(v)
                    enqueue(Q, v)
                    lk.add(new_e, (u, v))
            curr_e = curr_e.nextNode

    return Graph(G.v, new_e)

# Ejercicio 9
def DFS(G: Graph, s) -> Graph:
    v = G.v.head
    visited = []
    new_e = lk.LinkedList()

    def dfs_visit(G: Graph, u):
        visited.append(u)
        adj_u = G.graph.dictionary[G.graph.hash_func(u)].head
        while adj_u is not None:
            if isinstance(adj_u.value, tuple):
                v = adj_u.value[1]
                if v not in visited:
                    dfs_visit(G, v)
                    lk.add(new_e, (u, v))
            adj_u = adj_u.nextNode

    while v is not None:
        if v.value not in visited:
            dfs_visit(G, v.value)
        v = v.nextNode

    return Graph(G.v, new_e)

# Ejercicio 10
# (Sólo cuando los vértices son numéricos)
def bestRoad(G: Graph, v1, v2) -> lk.LinkedList|None:
    road = []

    if search(G.graph, v1) is None or search(G.graph, v2) is None:
        return build_list(road)

    visited = [v1]
    len_v = G.graph.m
    parent = [None] * len_v

    Q = lk.LinkedList()
    enqueue(Q, v1)
    while Q.head is not None:
        u = dequeue(Q)
        curr_e = G.graph.dictionary[G.graph.hash_func(u)].head
        while curr_e is not None:
            if isinstance(curr_e.value, tuple):
                v = curr_e.value[1]
                if v not in visited:
                    visited.append(v)
                    enqueue(Q, v)
                    parent[v - 1] = u
            curr_e = curr_e.nextNode

    index = v2 - 1
    while index != v1 - 1:
        road.append(parent[index])
        index = parent[index] - 1
    road.insert(0, v2)

    return build_list(road[::-1])

# Ejercicio 14
def PRIM(G: WeightedGraph) -> WeightedGraph:
    if G.v.head is None:
        return G

    T_e = []
    U = [G.v.head.value]
    len_v = G.graph.m

    while len(U) != len_v:
        min_weight = inf
        min_v = None
        min_u = None
        for u in U:
            curr_v = G.graph.dictionary[G.graph.hash_func(u)].head
            if curr_v is None:
                continue
            curr_v = curr_v.nextNode
            while curr_v is not None:
                if isinstance(curr_v.value, tuple) and isinstance(curr_v.value[1], tuple):
                    v, w = curr_v.value[1]
                    if v not in U and w < min_weight:
                        min_weight = w
                        min_v = v
                        min_u = u
                curr_v = curr_v.nextNode
        U.append(min_v)
        T_e.append((min_u, min_v, min_weight))
        
    return WeightedGraph(G.v, build_list(T_e))

# Ejercicio 15
def KRUSKAL(G: WeightedGraph) -> WeightedGraph:
    if G.v.head is None:
        return G

    T_e = []
    disjoint_set = DisjointSet(G.v)

    E = []
    curr_e = G.e.head
    while curr_e is not None:
        E.append(curr_e.value)
        curr_e = curr_e.nextNode
    E = sorted(E, key = lambda x: x[2])

    for edge in E:
        if disjoint_set.find_set(edge[0]) != disjoint_set.find_set(edge[1]):
            T_e.append(edge)
            disjoint_set.union(edge[0], edge[1])

    return WeightedGraph(G.v, build_list(T_e))


# Ejercicio 21
def initRelax(G: WeightedDirectedGraph, s, Q: list[tuple], distance: Dictionary, parent: Dictionary) -> None:
    curr_v = G.v.head
    while curr_v is not None:
        insert(distance, (curr_v.value, inf), key = curr_v.value)
        Q.insert(G.graph.hash_func(curr_v.value), (curr_v.value, inf))
        insert(parent, (curr_v.value, None), key = curr_v.value)
        curr_v = curr_v.nextNode
    delete(distance, s)
    insert(distance, (s, 0), key = s)
    Q[G.graph.hash_func(s)] = (s, 0)

def relax(G: WeightedDirectedGraph, Q: list[tuple], distance: Dictionary, parent: Dictionary, u, v) -> None:
    v_d = search(distance, v)
    u_d = search(distance, u)
    try:
        v_d = [node for node in Q if node[0] == v][0]
        u_d = [node for node in Q if node[0] == u][0]
    except IndexError:
        pass

    if v_d and u_d:
        v_d = v_d[1]
        u_d = u_d[1]
        w = None
        curr_e = G.graph.dictionary[G.graph.hash_func(u)].head
        if curr_e:
            curr_e = curr_e.nextNode
        while curr_e is not None:
            if isinstance(curr_e.value, tuple):
                v_j, weight = curr_e.value[1]
                if v_j == v:
                    w = weight
            curr_e = curr_e.nextNode

        if w is None:
            return

        if v_d > (u_d + w):
            delete(distance, v)
            delete(parent, v)
            insert(distance, (v, u_d + w), v)
            insert(parent, (v, u), v)
            for i, node in enumerate(Q):
                if node[0] == v:
                    Q[i] = (v, u_d + w)

def shortestPath(G: WeightedDirectedGraph, s, x) -> lk.LinkedList|None:
    if G.v.head is None:
        return None

    road = []

    distance = Dictionary(G.graph.m)
    Q = []
    parent = Dictionary(G.graph.m)

    initRelax(G, s, Q, distance, parent)

    S = []

    Q.sort(key = lambda x: x[1])

    while len(Q) > 0:
        u = Q[0][0]
        Q.pop(0)
        S.append(u)

        adj_u = G.graph.dictionary[G.graph.hash_func(u)].head
        if adj_u:
            adj_u = adj_u.nextNode
        while adj_u is not None:
            if not isinstance(adj_u.value, tuple):
                continue
            v = adj_u.value[1][0]
            if v not in S:
                relax(G, Q, distance, parent, u, v)
                Q.sort(key = lambda x: x[1])
            adj_u = adj_u.nextNode
    
    curr_parent = search(parent, x)
    while curr_parent is not None:
        road.append(curr_parent[1])
        curr_parent = search(parent, curr_parent[1])
    road.insert(0, x)
    road.pop()

    if len(road) == 1 and road[0] == x:
        return None

    return build_list(road[::-1])

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

def test_weighted_graph() -> WeightedGraph:
    print("--- weighted, undirected ---")
    v = build_list([1, 2, 3, 4, 5])
    e = build_list([
        (1, 2, 5),
        (1, 3, 2),
        (2, 4, 7),
        (3, 4, 1),
        (3, 5, 4),
        (4, 5, 3),
    ])
    graph = WeightedGraph(v, e)
    graph.printGraph()
    return graph

def test_weighted_directed_graph() -> WeightedDirectedGraph:
    print("--- weighted, directed ---")
    v = build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    e = build_list([
        (1, 2, 4),
        (1, 3, 2),
        (1, 4, 7),
        (2, 3, 1),
        (2, 5, 5),
        (2, 6, 8),
        (3, 2, 3),
        (3, 4, 3),
        (3, 5, 6),
        (4, 5, 2),
        (4, 7, 6),
        (5, 6, 1),
        (5, 7, 4),
        (5, 8, 7),
        (6, 3, 4),
        (6, 8, 3),
        (6, 9, 6),
        (7, 8, 2),
        (7, 10, 5),
        (8, 9, 1),
        (8, 10, 4),
        (9, 6, 2),
        (9, 10, 2),
        (10, 7, 3),
    ])
    graph = WeightedDirectedGraph(v, e)
    graph.printGraph()
    return graph
 
if __name__ == "__main__":
    graph1 = test_int_graph()
    graph2 = test_str_graph()
    graph3 = test_weighted_graph()
    graph4 = test_weighted_directed_graph()
    print()

    # print(existPath(graph1, 1, 4))
    # print()

    # print(isConnected(graph1))
    # print(isConnected(graph2))
    # print()

    # print(isTree(graph1))
    # print()

    # convertTree(graph1).print_list()
    # print()

    # print(countConnections(graph1))
    # print(countConnections(graph2))
    # print()

    # BFS(graph1, 3).printGraph()
    # print()

    # DFS(graph1, 1).printGraph()
    # print()
    # DFS(graph2, "A").printGraph()
    # print()

    # bestRoad(graph1, 1, 5).print_list()
    # print()

    # PRIM(graph3).printGraph()
    # print()

    # KRUSKAL(graph3).printGraph()
    # print()

    # shortestPath(graph4, 5, 4).print_list()
