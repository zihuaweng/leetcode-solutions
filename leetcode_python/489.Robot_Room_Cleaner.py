#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 这里面的上下左右位置很重要,否则会死循环
        self.dfs(robot, 0, 0, 0, set())

    def dfs(self, robot, x, y, cur, visited):
        robot.clean()
        visited.add((x, y))

        for k in range(4):
            next_x = x + self.directions[cur][0]
            next_y = y + self.directions[cur][1]
            if (next_x, next_y) not in visited and robot.move():
                self.dfs(robot, next_x, next_y, cur, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()

            robot.turnLeft()
            cur += 1
            cur %= 4











