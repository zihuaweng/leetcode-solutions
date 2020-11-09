class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        RX XL RXR XL

        XR LX XRR LX

        "XL" -> "LX"   L move to left, and could not pass next L or R
        "RX" -> "XR"   R move to right, and could not pass next L or R

        s: s[i] == 'L'
        e: e[j] == 'L'
        i >= j

        s: s[i] == 'R'
        e: e[j] == 'R'
        i <= j

        """
        if len(start) != len(end):
            return False
        start_list = [(i, s) for i, s in enumerate(start) if s == 'L' or s == 'R']
        end_list = [(j, e) for j, e in enumerate(end) if e == 'L' or e == 'R']
        if len(start_list) != len(end_list):
            return False
        
        for start_ele, end_ele in zip(start_list, end_list):
            i, s = start_ele
            j, e = end_ele
            if s != e:
                return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
        return True
        
    