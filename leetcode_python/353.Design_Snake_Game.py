# https://leetcode.com/problems/design-snake-game/

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = collections.deque([(0,0)])
        self.food = collections.deque(food)
        self.width = width
        self.height = height
        self.d = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
            
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        """
        1. check out of boundary
        2. deque to store snake, add to the top and delete the last one in the deque
        3. snake reach list in the queue also return -1
        3. board[i][j] == 'F', need to add to top without delete the laste one in the deque
        """
        x, y = self.snake[0]
        i = x+self.d[direction][0]
        j = y+self.d[direction][1]
        
        if i < 0 or i >= self.height or j < 0 or j >= self.width:  # check bounary
            return -1
        
        # print((i,j), self.board[i][j], self.count)
        if self.food and [i,j] == self.food[0]:
            self.snake.appendleft((i,j))
            self.food.popleft()
        else:
            self.snake.pop()
            if (i,j) in self.snake:    # reach to itself
                return -1
            else:
                self.snake.appendleft((i,j))
                
        return len(self.snake)-1
            
            
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)