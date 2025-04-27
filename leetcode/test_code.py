#  Copyright (c) 2025.
#  @Author Subhrajeet Ghosh
def marbles_distribution(weights, k):
    n = len(weights)

    # Edge cases
    if k == 1:
        return 0  # Only one bag, score is fixed (weights[0] + weights[n-1])
    if n < k:
        return 0  # Impossible to split into k non-empty bags

    # Recursive function: returns (min_score, max_score) for given start and bags_left
    def distribute(start, bags_left):
        # Base case: one bag left, use all remaining marbles
        if bags_left == 1:
            if start >= n:
                return float('inf'), float('-inf')  # Invalid
            score = weights[start] + weights[n - 1]
            return score, score

        # If not enough marbles for remaining bags
        remaining = n - start
        if remaining < bags_left:
            return float('inf'), float('-inf')  # Invalid

        min_score = float('inf')
        max_score = float('-inf')

        # Try all possible end points for the current bag
        # Bag must have at least 1 marble, and leave enough for remaining bags
        for end in range(start, n - bags_left + 1):  # Ensure enough marbles left
            current_cost = weights[start] + weights[end]
            # Recursively solve for remaining marbles and bags
            sub_min, sub_max = distribute(end + 1, bags_left - 1)
            if sub_min != float('inf'):  # Valid subproblem
                total_min = current_cost + sub_min
                total_max = current_cost + sub_max
                min_score = min(min_score, total_min)
                max_score = max(max_score, total_max)

        return min_score, max_score

    # Start recursion from index 0 with k bags
    min_score, max_score = distribute(0, k)
    return max_score - min_score if min_score != float('inf') else 0


# Test cases
print(marbles_distribution([1, 3, 5, 1], 2))  # Expected: 4
print(marbles_distribution([1, 3], 2))  # Expected: 0 (n = k)
print(marbles_distribution([1, 2, 3], 1))  # Expected: 0 (k = 1)
print(marbles_distribution([1, 3, 5, 2, 1], 3))  # Expected: 8
