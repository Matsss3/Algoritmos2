from dictionary import *
import random

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

# Ejercicio 6
def postal_hash(postal_code: str) -> tuple[tuple[int, int], int]:
    m = 10009
    # Maximo valor: Z9999ZZZ => 
    # 122*10⁷ + 9*10⁶ + 9*10⁵ + 9*10⁴ + 9*10³ + 122*10² + 122*10¹ + 122*10⁰
    # 1.230.195.542, primo mayor => 1230195553
    p = 1230195553
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    c = 10000

    encoded = 0
    for ch in postal_code:
        if ch.isdigit():
            encoded += int(ch)
        else:
            encoded += ord(ch)

    key = ((a * encoded + b) % p) % m

    return ((a, b), key)

# print(postal_hash("C1024CWN"))
# print(postal_hash("A6927VOW"))
# print()

# Ejercicio 7
def hash_compression(s: str) -> str:
    m = len(s) if len(s) < 122 else 122
    counts = Dictionary(m)
    result = ""

    for ch in s:
        if search(counts, ord(ch)) is not None:
            key = counts.hash_func(ord(ch))
            counts.dictionary[key].head.value[1] += 1
        else:
            insert(counts, ord(ch), 1)

    for slot in counts.dictionary:
        if slot.head is not None:
            key = counts.hash_func(slot.head.value[0])
            amount = slot.head.value[1]
            result += f"{chr(slot.head.value[0])}{amount}"

    return result if len(result) < len(s) else s

def normal_compression(s: str) -> str:
    result = ""
    i = 0

    while i < len(s):
        current = s[i]
        count = 0
        while i < len(s) and s[i] == current:
            count += 1
            i += 1
        result += f"{current}{count}"

    return result if len(result) < len(s) else s

# print(hash_compression("aabcccccaaa"))
# print(normal_compression("aabcccccaaa"))
# print()

# Ejercicio 8
def find_substr(s: str, substr: str) -> None|int:
    if len(s) < len(substr):
        return None

    p = 23
    processed = [ord(s[0])]

    for i in range(1, len(s)):
        processed.append(processed[i - 1] + ord(s[i]) * (p ** i))
    processed.insert(0, 0)
    
    substr_hash = sum([ord(ch) * (p ** i) for i, ch in enumerate(substr)])
    sub_len = len(substr)
    
    for pref in range(sub_len, len(processed)):
        if (processed[pref] - processed[pref - sub_len]) // (p ** (pref - sub_len)) == substr_hash:
            return pref - sub_len

    return None

# print(find_substr("abracadabra", "cada"))
# print(find_substr("holamundo", "undo"))
# print()
