# 如果需要在中间返回结果，使用下面模板：
def bs(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if check(mid) == target:
            return mid
        elif check(mid) < target:
            left = mid + 1
        else:
            right = mid - 1

# 如果需要返回index，使用下面模板：
# 这样的写法终止条件是left==right, 区间就剩下一个元素，所以如果有结果一定是left，如果left不对，那就返回默认值

def bs(arr):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left+right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid

def bs(arr):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left+right+1) // 2  # 看到left=mid，就需要上取整！不然会进入死循环
        if check(mid):
            right = mid - 1
        else:
            left = mid   

# mid = (left+right+1) // 2 的原因：
# 如果最后剩下两个元素，我们有left=mid，而(left+right) // 2 会给我们上区间，就是left的位置，所以
# 所以mid最后还是会等于left，就产生死循环，所以+1后我们可以得到下区间，退出循环。


# 寻找边界
def bisect_right(a, x):
    """寻找右边界，所有左边数, a[:i]小于等于x, 所有右边数, a[i:], 大于x.
    """
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo



def bisect_left(a, x):
    """寻找左边界，所有左边数, a[:i]小于x, 所有右边数, a[i:], 大于等于x.
    """

    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# 需要精确到一个小数点范围
# calculate root
def root(x, n):
  if x == 0:
    return 0
  
  low = 0
  hi = max(1, x)
  root = (low+hi) / 2.0
  
  while root - low > 0.001:   # 小数点范围限制
    if root**n > x:
      hi = root
    elif root**n < x:
      low = root
    else:
      break
    root = (low+hi) / 2.0
    
  return root


# 需要精确到一个小数点范围
def minmaxGasDist(self, stations: List[int], K: int) -> float:
        
    def valid(mid):
        pass
    
    i = 0
    j = stations[-1]-stations[0]
    while j - i > 1e-6:
        mid = (i+j) / 2
        if valid(mid):
            j = mid
        else:
            i = mid
            
    return i

