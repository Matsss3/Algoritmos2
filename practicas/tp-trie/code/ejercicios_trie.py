from trie import *

# Ejercicio 4
def trie_prefix(T: Trie, p: str, n: int) -> list[str]:
    if T.root is None or T.root.children.head is None:
        return []

    if n < len(p):
        return []

    pref = p
    current = T.root
    node = current.children.head

    while node is not None:
        if node.value.key == pref[0]:
            pref = pref[1:]
            current = node.value
            if pref == "":
                break
            node = node.value.children.head
            continue
        node = node.nextNode

    if pref != "":
        return []

    suf = n - len(p)

    def _append_suffix(node_rec: TrieNode|None, k: int) -> list[str]:
        if node_rec is None:
            return []

        if k == 0:
            return [node_rec.key]

        words = []
        curr = node_rec.children.head
        while curr is not None:
            words_child = _append_suffix(curr.value, k - 1)
            for w in words_child:
                words.append(node_rec.key + w)
            curr = curr.nextNode

        return words

    suffixes = _append_suffix(current, suf)
    return [p + w[1:] for w in suffixes]

# Ejercicio 5
def matching_tries(T1: Trie, T2: Trie) -> bool:
    return _matching_tries(T1.root, T2.root)

def _matching_tries(node1: TrieNode|None, node2: TrieNode|None) -> bool:
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1.isEndOfWord != node2.isEndOfWord:
        return False

    cl1 = node1.children.head
    cl2 = node2.children.head
    while cl1 is not None and cl2 is not None:
        if cl1.value.key != cl2.value.key:
            return False
        if cl1.value.isEndOfWord != cl2.value.isEndOfWord:
            return False
        if not _matching_tries(cl1.value, cl2.value):
            return False

        cl1 = cl1.nextNode
        cl2 = cl2.nextNode

    if cl1 is not None or cl2 is not None:
        return False

    return True

# Ejercicio 6
def inverted_trie(T: Trie, element: str) -> bool:
    if element == "":
        return True

    if T.root is None or T.root.children.head is None:
        return False
    
    inverted = element[::-1]

    if search(T, element) and search(T, inverted):
        return True

    return False
        
# ========== TESTING ==========
def build_trie(words):
    trie = Trie()
    for w in words:
        insert(trie, w)
    return trie

TEST_CASES = {
    "empty":          [],
    "single_word":    ["cat"],
    "shared_prefix":  ["car", "rac", "cart", "care", "cat"],
    "shared_prefix2":  ["care", "car", "cat", "cart", "rac"],
    "prefix_is_word": ["an", "and", "ant", "a"],
    "disjoint":       ["dog", "zebra", "apple"],
    "mixed":          ["tea", "ten", "to", "inn", "in", "i"],
    "prefixes":       [
                        "trans",
                        "transfer",
                        "transformation",
                        "transport",
                        "transportation",
                        "transparent",
                        "transformer",
                        "transferring",
                        "transnational",
                        "transparency",
                      ]
}

if __name__ == "__main__":
    t = build_trie(TEST_CASES["prefixes"])
    t2 = build_trie(TEST_CASES["shared_prefix"])
    t3 = build_trie(TEST_CASES["prefixes"])
    t4 = build_trie(TEST_CASES["shared_prefix2"])

    # t2.print_trie()
    # t4.print_trie()
    #
    # print(matching_tries(t, t3))
    # print(matching_tries(t2, t4))
    #
    # print()
    # t.print_trie()
    # print(trie_prefix(t, "trans", 9))

    # print()
    # print(inverted_trie(t2, "car"))
    # print(inverted_trie(t, "transport"))
