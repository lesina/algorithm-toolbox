# Uses python3

from itertools import chain, islice


def suffix_array(A):
    """Return a list of the starting positions of the suffixes of the
    sequence A in sorted order.

    For example, the suffixes of ABAC, in sorted order, are ABAC, AC,
    BAC and C, starting at positions 0, 2, 1, and 3 respectively:

    >>> suffix_array('ABAC')
    [0, 2, 1, 3]

    """
    # This implements the algorithm of Vladu and Negruşeri; see
    # http://web.stanford.edu/class/cs97si/suffix-array.pdf

    L = sorted((a, i) for i, a in enumerate(A))
    n = len(A)
    count = 1
    while count < n:
        # Invariant: L is now a list of pairs such that L[i][1] is the
        # starting position in A of the i'th substring of length
        # 'count' in sorted order. (Where we imagine A to be extended
        # with dummy elements as necessary.)

        P = [0] * n
        for (r, i), (s, j) in zip(L, islice(L, 1, None)):
            P[j] = P[i] + (r != s)

        # Invariant: P[i] is now the position of A[i:i+count] in the
        # sorted list of unique substrings of A of length 'count'.

        L = sorted(chain((((P[i],  P[i+count]), i) for i in range(n - count)),
                         (((P[i], -1), i) for i in range(n - count, n))))
        count *= 2
    return [i for _, i in L]

text = input()
print(*suffix_array(text))