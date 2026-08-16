# RadixSort ordena los elementos de la lista usando como criterio
# el dígito menos significativo por cada pasada, empezando por el
# lugar de las unidades, decenas, centesimas, etc. Siendo n el numero
# de elementos en la lista a ordenar y k la cantidad de dígitos en 
# el número más grande de la lista, su complejidad temporal es siempre
# O(nk), por lo que no hay peor, mejor o caso promedio. Esto se debe
# a que se itera la lista una vez (como se ve en counting_sort) por cada
# dígito del número más grande de la lista (en radix_sort).

def radix_sort(A: list):
    max_num = max(A)
    place = 1
    while max_num // place > 0:
        counting_sort(A, place)
        place *= 10

def counting_sort(A: list, place: int):
    n = len(A)
    output = [0] * n
    count = [0] * 10

    for num in A:
        digit = (num // place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (A[i] // place) % 10
        output[count[digit] - 1] = A[i]
        count[digit] -= 1

    for i in range(n):
        A[i] = output[i]


numbers = [170, 45, 75, 90, 802, 24, 2, 66]

radix_sort(numbers)

print(numbers)
