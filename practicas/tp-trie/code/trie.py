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
    if element == "":
        return

    if T.root is None:
        T.root = TrieNode(None)
        word_node = build_word(element)
        if word_node:
            word_node.parent = T.root
            lk.add(T.root.children, word_node)
        return

    word = element
    current = T.root
    cl = current.children.head

    while cl is not None:
        if word == "" or cl.value.key == word[0]:
            word = word[1:]
            if word == "":
                cl.value.isEndOfWord = True
                return

            current = cl.value

            if cl.value.children.head is None:
                word_node = build_word(word)
                if word_node:
                    word_node.parent = current
                    lk.add(current.children, word_node)
                return

            cl = cl.value.children.head
            continue
        cl = cl.nextNode

    word_node = build_word(word)
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

def search(T: Trie, element: str) -> bool:
    if T.root is None or T.root.children.head is None:
        if element == "":
            return True
        else:
            return False

    word = element
    cl = T.root.children.head

    while cl is not None:
        if word == "" or cl.value.key == word[0]:
            word = word[1:]
            if word == "":
                if cl.value.isEndOfWord:
                    return True
                else:
                    return False
            cl = cl.value.children.head
            continue
        cl = cl.nextNode

    return False

# Ejercicio 3
def delete(T: Trie, element: str) -> bool:
    if T.root is None or T.root.children.head is None:
        if element == "":
            return True
        else:
            return False

    if element == "":
        return False

    word = element
    current = T.root
    cl = current.children.head

    while cl is not None:
        if word == "" or cl.value.key == word[0]:
            current = cl.value
            word = word[1:]
            if word == "":
                if current.isEndOfWord:
                    break
                else:
                    return False
            cl = cl.value.children.head
            continue
        cl = cl.nextNode

    if word != "":
        return False

    if current:
        if current.children.head is None:
            node = None
            while (current.parent is not None and 
                   (lk.length(current.children) == 1
                    or lk.length(current.children) == 0)):
                node = current
                current = current.parent
                if current.isEndOfWord:
                    break
            lk.delete(current.children, node)
        else:
            current.isEndOfWord = False

        return True
    else:
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
    "shared_prefix":  ["car", "cart", "care", "cat"],
    "prefix_is_word": ["an", "and", "ant", "a"],
    "disjoint":       ["dog", "zebra", "apple"],
    "mixed":          ["tea", "ten", "to", "inn", "in", "i"],
}

if __name__ == "__main__":
    for name, words in TEST_CASES.items():
        print(f"\n{name}: {words}")
        t = build_trie(words) if words else Trie()
        t.print_trie()

    t = build_trie(TEST_CASES["shared_prefix"])
    print(search(t, "cart"))
    print(search(t, "car"))
    print(search(t, "cares"))

    t.print_trie()

    delete(t, "care")
    print()
    t.print_trie()
