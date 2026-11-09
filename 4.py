def solution(A):
    S = set()

    for value in A:
        # Store each absolute value only once.
        S.add(abs(value))

    return len(S)
