def max_heapify(list, i, n): # rendre l'arbre à i un max heap
    l = 2*i
    r = 2*i+1

    largest = i
    if l <= n and list[l] > list[i]:
        largest = l
    if r <= n and list[r] > list[largest]:
        largest = r

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        max_heapify(list, largest, n)

def build_max_heap(list, n):
    for i in range(n//2, 0, -1):
        max_heapify(list, i, n)
    return list

def heapsort(list, n):
    build_max_heap(list, n)
    for i in range(n, 1, -1):
        list[1], list[i] = list[i], list[1]
        max_heapify(list, 1, i-1)
        

if __name__ == "__main__":
    # -1 is just a prefix: the list starts at index 1

    # Heap sort test
    list = [-1, 1, 100,3,4,2,9]
    heapsort(list, len(list)-1)
    assert list == [-1,1,2,3,4,9,100]

    print("All tests passed.")