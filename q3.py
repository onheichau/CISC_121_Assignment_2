def solution(A):
    # handle trivial case
    if len(A) < 3:
        return 0

    A.sort()

    # start scanning by 3 elements at a time
    for i in range(len(A) - 2):
        if A[i] <= 0:
            continue

        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0
