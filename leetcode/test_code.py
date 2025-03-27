#  Copyright (c) 2025.
#  @Author Subhrajeet Ghosh
def count_special_vegetables_optimized(A):

    N = len(A)

    if N == 0:

        return 0

    # Precompute prefix sums for even and odd indices

    prefix_even = [0] * N

    prefix_odd = [0] * N

    for i in range(N):

        if i == 0:

            prefix_even[i] = A[i] if i % 2 == 0 else 0

            prefix_odd[i] = A[i] if i % 2 != 0 else 0

        else:

            prefix_even[i] = prefix_even[i - 1] + (A[i] if i % 2 == 0 else 0)

            prefix_odd[i] = prefix_odd[i - 1] + (A[i] if i % 2 != 0 else 0)

    special_count = 0

    # For each removal, recalculate the sums after re-indexing

    for i in range(N):

        # Left part: elements before index i (unchanged order)

        left_even = prefix_even[i - 1] if i > 0 else 0

        left_odd = prefix_odd[i - 1] if i > 0 else 0

        # Right part: elements after index i

        # When removed, these shift left by one:

        # For j > i in original array, the new index is (j - 1).

        # New even positions in the right part come from original odd indices.

        # New odd positions in the right part come from original even indices.

        right_even = prefix_even[N - 1] - prefix_even[i]

        right_odd = prefix_odd[N - 1] - prefix_odd[i]

        # New cart sums after removal:

        even_sum = left_even + right_odd    # left even indices + shifted right odd indices

        odd_sum = left_odd + right_even     # left odd indices + shifted right even indices

        if even_sum == odd_sum:

            special_count += 1

    return special_count

# Example Test Case
A = [2,1,6,4]  # Sample array
print(count_special_vegetables_optimized(A))  # Output: Count of special vegetables


#MAE: 17665.120684931506