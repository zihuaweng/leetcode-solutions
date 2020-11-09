# https://leetcode.com/problems/longest-absolute-file-path/


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32

        dir
            \tsubdir1
                \t\tfile1.ext
                \t\tsubsubdir1
            \tsubdir2
                \t\tsubsubdir2
                \t\t\tfile2.ext
                
        put each in one line (split using '\n')
        record the level
            dir has 0 '\t' is level 0,
            \tsubdir1 has 1 '\t' is level 1,
            \t\tfile1.ext has 2 is level 2
                -> this contains '.' so it is file. if we find file, we need to add all its previous level to the file length
                -> file_len + d[0] + d[1]
        """
        d = {}
        max_len = 0
        paths = input.split('\n')
        for path in paths:
            count = path.count('\t')  # count '\t' to know whic level
            length = len(path) - count
            if '.' in path:
                for i in range(count):
                    length += d[i] + 1   # + 1 casue we need to add '/' at the end of dir
                max_len = max(max_len, length)
            else:
                d[count] = len(path) - count
                
        return max_len
                
        