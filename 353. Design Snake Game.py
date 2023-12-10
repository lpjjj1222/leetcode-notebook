class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
    
        self.snake_set = set()
        self.snake_set.add((0,0))
        self.snake = collections.deque([(0,0)])
        self.food_index = 0
        self.movement = {'U': [-1,0], 'L':[0,-1], 'R':[0,1], 'D':[1,0]}
   
    def move(self, direction: str) -> int:
        #新头
        newHead = (self.snake[0][0] + self.movement[direction][0],
                    self.snake[0][1] + self.movement[direction][1])
        #判断新头是否出边界
        cross_column_limit = newHead[0] < 0 or newHead[0] >= self.height
        cross_row_limit = newHead[1] < 0 or newHead[1] >= self.width

        #判断🐍是否会咬到自己
        #判断新头是否已存在自己的队列里 除了尾巴，因为最后一个格子每次都会消失 除非是吃东西
        #但吃东西并不会咬到自己，因为题目规定食物不会放在有蛇身体的格子上
        bite_itself = newHead in self.snake and newHead != self.snake[-1]

        if cross_column_limit or cross_row_limit or bite_itself:
            return -1
        #_____________________________________________________________________
        
        #确定食物的位置
        food_location = self.food[self.food_index] if self.food_index < len(self.food) else None
        #如果食物就在新头的位置，就吃掉
        if food_location and food_location[0] == newHead[0] and food_location[1] == newHead[1]:
            self.food_index += 1
        else: #如果该move并不会吃掉食物则要把尾巴删掉
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        self.snake_set.add(newHead)
        self.snake.appendleft(newHead)

        return len(self.snake) - 1


        





        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
