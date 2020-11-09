# https://leetcode.com/problems/rectangle-area/



class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = (C-A)*(D-B) + (G-E)*(H-F)
        h = min(D, H) - max(B, F)
        w = min(C, G) - max(A, E)
        if h > 0 and w > 0:
            return area - h*w
        return area