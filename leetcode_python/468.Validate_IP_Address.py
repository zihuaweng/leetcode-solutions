#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            if len(IP.split('.')) != 4:
                return "Neither"
            for n in IP.split('.'):
                if not n.isdigit() or str(int(n)) != n or int(n) < 0 or int(n) > 255:
                    return "Neither"
            return "IPv4"

        if ':' in IP:
            ip = IP.split(':')
            if len(ip) != 8:
                return "Neither"
            for n in IP.split(':'):
                if len(n) > 4 or not re.match("^[a-fA-F0-9]+$", n):
                    return "Neither"
            return "IPv6"

        return "Neither"