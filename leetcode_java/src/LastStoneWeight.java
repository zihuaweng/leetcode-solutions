//https://leetcode.com/problems/last-stone-weight/

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
//        the same
//        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> y - x);
        for (int n: stones) {
            pq.add(n);
        }
        while (pq.size() > 1) {
            int a = pq.poll();
            int b = pq.poll();
            if (a != b) {
                pq.add(Math.abs(a-b));
            }
        }
        return pq.isEmpty()? 0 : pq.poll();
    }
}