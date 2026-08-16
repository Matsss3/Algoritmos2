def contiene_suma(A: list, n: int) -> bool:
    if n == 0:
        return True
    vistos = set()
    for i in A:
        if n - i in vistos:
            return True
        vistos.add(i)
    return False

assert contiene_suma([1, 2, 3, 4, 5], 7) == True
assert contiene_suma([1, 2, 3, 4, 5], 20) == False
assert contiene_suma([1, 1, 3, 7], 2) == True
assert contiene_suma([1, 3, 7], 2) == False
assert contiene_suma([-5, -2, 1, 4, 10], -1) == True
assert contiene_suma([-10, -3, 2, 7, 15], 5) == True
assert contiene_suma([0, 0, 1, 2], 0) == True
assert contiene_suma([], 5) == False
assert contiene_suma([5], 10) == False
assert contiene_suma([10**9, -10**9, 123, 456], 0) == True
assert contiene_suma([10, 20, 1, 50, 100], 30) == True
assert contiene_suma([1, 5, 8, 20, 30, 70], 100) == True
assert contiene_suma([5, 5, 5, 5, 5], 10) == True
assert contiene_suma([-10, -8, -3, 1, 4], -7) == True
assert contiene_suma([9, 1, 20, -4, 7, 3], 16) == True

# Complejidad O(n), ya que itera la lista una sola vez.
