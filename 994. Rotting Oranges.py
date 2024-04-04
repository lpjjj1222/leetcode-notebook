class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #遍历所有格子数fresh的个数，并把烂橘子放进deque里
        #当deque()还有橘子并且fresh的个数>0则进入while循环
        # minutes即层数，看到第几层时fresh的个数减到0
        #for _ in range(len(q))记录一层橘子的个数，每一层minutes加1
        
        nRow = len(grid)
        nCol = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(nRow):
            for j in range(nCol):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                x , y = q.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < nRow and 0 <= ny < nCol and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
                        fresh -= 1
        if fresh > 0:
            return -1
        return minutes

        



        