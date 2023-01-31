def solution(lst):
    alldigits = ''.join(map(str, lst))
    counts = [0] * 10
    for digit in alldigits:
        counts[int(digit)] += 1
    maxcount = max(counts)
    return [digit for digit, count in enumerate(counts) if count == maxcount]

