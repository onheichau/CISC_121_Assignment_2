from heapq import heapify, heappop


def solution(A):
    min_heap = list(A)
    max_heap = [-value for value in A]
    heapify(min_heap)
    heapify(max_heap)

    # Undo the negation as we pop the three largest values.
    largest, second_largest, third_largest = [-heappop(max_heap) for _ in range(3)]

    # Keep both entries even if they have the same value.
    smallest, second_smallest = [heappop(min_heap) for _ in range(2)]

    return max(
        largest * second_largest * third_largest,
        largest * smallest * second_smallest,
    )
