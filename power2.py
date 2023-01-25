'''Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.

Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of 2.'''


def solution(numbers):
    # stores the count of valid pairs
    count = 0

    # computes the target powers of two using bit shifts
    targets = [1] + [1 << i for i in range(1, 31)]

    # keeps track of values we've seen so far. used to search for target complements
    seen = set()

    # step through the numbers once, in reverse
    for n in numbers[::-1]:
        # add the current number to the hashset
        seen.add(n)

        # scan through all potential targets
        for t in targets:
            # if this complement is in the map, it means we've found a valid pair
            if (t - n) in seen:
                count += 1

        ## finding the count of valid pairs in one go with a generator
        # count += sum(t - n in seen for t in targets)

    return count