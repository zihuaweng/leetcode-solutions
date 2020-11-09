#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

# https://leetcode.com/problems/exclusive-time-of-functions/


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        d = [0] * n
        stack = []
        
        prev_time = 0
        
        for log in logs:
            job, state, time = log.split(':')
            job = int(job)
            time = int(time)
            
            if state == 'start':
                if stack:
                    d[stack[-1]] += time - prev_time 
                stack.append(job)
                prev_time = time
            else:
                d[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
                
        return d



class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        d = [0] * n
        stack = []
        
        for log in logs:
            job, state, time = log.split(':')
            job = int(job)
            time = int(time)
            
            if state == 'start':
                stack.append((job, time))
            else:
                start = stack.pop()[1]
                duration = time - start + 1
                d[job] += duration
                
                if stack:
                    d[stack[-1][0]] -= duration   # 需要减去被别的任务占用的时间
                
        return d