#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/reorder-data-in-log-files/


# Time complexity: O()
# Space complexity: O()


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            first, rest = log.split(" ", 1)
            return (0, rest, first) if rest[0].isalpha() else (1,)
        return sorted(logs, key = f)


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []

        for log in logs:
            array = log.split(' ')
            if array[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: x.split()[0])
        letter.sort(key=lambda x: x.split()[1:])
        return letter + digit