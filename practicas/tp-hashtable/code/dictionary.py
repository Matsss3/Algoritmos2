import linkedlist as lk
import math

class Dictionary:
    def __init__(self, m: int) -> None:
        self.m = m
        self.dictionary = [lk.LinkedList() for i in range(m)]

    def hash_func(self, key: int) -> int:
        return key % self.m

# Ejercicio 2
def insert(D: Dictionary, key: int, value) -> Dictionary:
    if key < 0:
        return D
    
    hashed_key = D.hash_func(key)
    lk.add(D.dictionary[hashed_key], (key, value))
    return D

def search(D: Dictionary, key: int):
    if key < 0:
        return None

    hashed_key = D.hash_func(key)
    current = D.dictionary[hashed_key].head
    while current is not None:
        if current.value[0] == key:
            return current.value[1]
        current = current.nextNode

    return None

def delete(D: Dictionary, key: int) -> Dictionary:
    if key < 0:
        return D

    hashed_key = D.hash_func(key)
    col_list = D.dictionary[hashed_key]
    current = col_list.head
    while current is not None:
        if current.value[0] == key:
            lk.delete(col_list, current.value)
            break
        current = current.nextNode
    
    return D

