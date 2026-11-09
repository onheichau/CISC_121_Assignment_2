def solution(A):
    S = set()

    for value in A:
        # Adding a value already in the set leaves its size unchanged.
        S.add(value)

    return len(S)
