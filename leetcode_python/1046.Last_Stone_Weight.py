# https://leetcode.com/problems/last-stone-weight/

# priority queue
# Time complexity:  O(nlogn)
# Space complexity:  O(n)

# insort
# Time complexity:  O(n^2)
# Space complexity:  O(n)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        pq = [-i for i in stones]
        heapq.heapify(pq)
        for i in range(len(stones) - 1):
            # 这里一种办法是便利stones然后每次合并0还是照样加进去，比较快，空间稍多
            # 或者也可以while len(pq) > 1，这样每次合并是0就去掉，与上面相反
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))

        return -pq[0]

    def lastStoneWeight2(self, stones):
        import bisect
        stones = sorted(stones)
        for _ in range(len(stones) - 1):
            x, y = stones.pop(), stones.pop()
            bisect.insort(stones, abs(x - y))
        return stones.pop()