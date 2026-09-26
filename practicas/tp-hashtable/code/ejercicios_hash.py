from dictionary import *

# Ejercicio 4
def is_perm(s: str, p: str) -> bool:
    if len(s) != len(p):
        return False

    hash_table = Dictionary(26)

    for ch in s:
        insert(hash_table, ord(ch), ch)

    for ch in p:
        delete(hash_table, ord(ch))

    for slot in hash_table.dictionary:
        if slot.head is not None:
            return False

    return True

# print(is_perm("hola", "aloh"))
# print(is_perm("hola", "chau"))
# print()

# Ejercicio 5
def contains_repeated(L: list[int]) -> bool:
    length = len(L)

    if length == 0:
        return False

    hash_table = Dictionary(length)

    for el in L:
        insert(hash_table, el, el)

    for slot in hash_table.dictionary:
        if slot.head and slot.head.nextNode is not None:
            return True

    return False
    
# print(contains_repeated([1,2,3,4,5]))
# print(contains_repeated([1,2,3,4,1]))
# print()
