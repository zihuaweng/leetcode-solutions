#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r

class BIT:
    """Implementation of a Binary Indexed Tree (Fennwick Tree)"""

    # def __init__(self, list):
    #    """Initialize BIT with list in O(n*log(n))"""
    #    self.array = [0] * (len(list) + 1)
    #    for i, val in enumerate(list):
    #        self.update(i, val)

    def __init__(self, list):
        """"Initialize BIT with list in O(n)"""
        self.array = [0] + list
        for i in range(1, len(self.array)):
            i2 = i + (i & -i)
            print(i, bin(i), bin(-i), i & -i, i2)
            if i2 < len(self.array):
                self.array[i2] += self.array[i]

    def prefix_query(self, i):
        """Computes prefix sum of up to including the i-th element"""
        i += 1
        result = 0
        while i:
            result += self.array[i]
            i -= i & -i
        return result

    def range_query(self, from_i, to_i):
        """Computes the range sum between two indices (both inclusive)"""
        return self.prefix_query(to_i) - self.prefix_query(from_i - 1)

    def update(self, i, add):
        """Add a value to the i-th element"""
        i += 1
        while i < len(self.array):
            self.array[i] += add
            i += i & -i


if __name__ == '__main__':
    array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    bit = BIT(array)
    print(bit.array)
    print('Array: [{}]'.format(', '.join(map(str, array))))
    print()

    print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
    print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
    print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
    print()

    bit.update(4, 2)
    print('Add {} to element at pos {}'.format(2, 4))
    new_array = [bit.range_query(i, i) for i in range(len(array))]
    print('Array: [{}]'.format(', '.join(map(str, new_array))))
    print()

    print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
    print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
    print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
    print()