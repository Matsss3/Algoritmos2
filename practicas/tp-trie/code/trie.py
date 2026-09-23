import linkedlist as lk

class Trie:
    def __init__(self) -> None:
        self.root: TrieNode|None = None

    def iter_children(self, node):
        current = node.children.head
        while current != None:
            yield current.value
            current = current.nextNode


    def print_trie(self):
        if self.root is None:
            print("(empty trie)")
            return
        print("(root)" + ("*" if self.root.isEndOfWord else ""))
        self._print_node(self.root, prefix="")

    def _print_node(self, node, prefix):
        children = list(self.iter_children(node))
        for i, child in enumerate(children):
            last = i == len(children) - 1
            branch = "└── " if last else "├── "
            mark = "*" if child.isEndOfWord else ""
            print(f"{prefix}{branch}{child.key}{mark}")
            self._print_node(child, prefix + ("    " if last else "│   "))

    def add_child(self, parent, key):
        child = TrieNode(key)
        child.parent = parent
        lk.add(parent.children, child)
        return child

class TrieNode:
    def __init__(self, key) -> None:
        self.parent: TrieNode|None = None
        self.children: lk.LinkedList = lk.LinkedList()
        self.key = key
        self.isEndOfWord: bool = False

# Ejercicio 1
def insert(T: Trie, element: str) -> None:
    if T.root is None:
        T.root = TrieNode(None)
        word_node = build_word(element)
        if word_node:
            word_node.parent = T.root
            lk.add(T.root.children, word_node)
        return

    counter = 0
    current = T.root
    cl = current.children.head

    while cl is not None:
        if cl.value.key == element[counter]:
            if counter == len(element) - 1:
                cl.value.isEndOfWord = True
                return

            counter += 1
            current = cl.value

            if cl.value.children.head is None:
                word_node = build_word(element[counter:])
                if word_node:
                    word_node.parent = current
                    lk.add(current.children, word_node)
                return

            cl = cl.value.children.head
            continue
        cl = cl.nextNode

    word_node = build_word(element[counter:])
    if word_node:
        word_node.parent = current
        lk.add(current.children, word_node)

def build_word(word: str) -> TrieNode|None:
    if word == "":
        return None

    first = TrieNode(word[0])
    current = first
    for ch in word[1:]:
        node = TrieNode(ch)
        node.parent = current
        lk.add(current.children, node)
        current = node
    current.isEndOfWord = True

    return first



# ========== TESTING ==========
def build_trie(words):
    trie = Trie()
    for w in words:
        insert(trie, w)
    return trie

TEST_CASES = {
    "empty":          [],
    "single_word":    ["cat"],
    "shared_prefix":  ["car", "cart", "care", "cat"],
    "prefix_is_word": ["a", "an", "and", "ant"],
    "disjoint":       ["dog", "zebra", "apple"],
    "mixed":          ["tea", "ten", "to", "inn", "in", "i"],
}

if __name__ == "__main__":
    for name, words in TEST_CASES.items():
        print(f"\n{name}: {words}")
        t = build_trie(words) if words else Trie()
        t.print_trie()
