# Time complexity: O()
# Space complexity: O()

# Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.


"""Bisection algorithms."""



def bisect_right(a, x, lo=0, hi=None):
    """寻找右边界，所有左边数, a[:i]小于等于x, 所有右边数, a[i:], 大于x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    a[mid] > x: hi = mid
    a[mid] == x: lo = mid + 1
    a[mid] < x: lo = mid + 1

    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo



def bisect_left(a, x, lo=0, hi=None):
    """寻找左边界，所有左边数, a[:i]小于x, 所有右边数, a[i:], 大于等于x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    a[mid] > x: hi = mid
    a[mid] == x: hi = mid
    a[mid] < x: lo = mid + 1
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Overwrite above definitions with a fast C implementation
try:
    from _bisect import *
except ImportError:
    pass

# Create aliases
bisect = bisect_right
insort = insort_right
