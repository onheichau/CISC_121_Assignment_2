def solution(A):
    # Sort so moving either pointer changes the sum predictably.
    A.sort()

    left = 0
    right = len(A) - 1
    best = float("inf")

    # Equality allows using the same element twice, as the problem permits.
    while left <= right:
        current_sum = A[left] + A[right]

        # Record the smallest absolute sum found so far.
        best = min(best, abs(current_sum))

        if current_sum == 0:
            # Zero is the smallest possible absolute sum.
            return 0
        elif current_sum < 0:
            # Increase the sum by moving to a larger left value.
            left += 1
        else:
            # Decrease the sum by moving to a smaller right value.
            right -= 1

    return best
