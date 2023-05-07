def heap_sort(arr):
    n = len(arr)
    # 부모 노드의 값이 자식 노드의 값보다 크거나 같은 최대 힙을 구축
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i  # 최대 힙을 루트로 선정
    left = 2 * i + 1  # 왼쪽 자식
    right = 2 * i + 2  # 오른쪽 자식

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트가 아닐 경우
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)
