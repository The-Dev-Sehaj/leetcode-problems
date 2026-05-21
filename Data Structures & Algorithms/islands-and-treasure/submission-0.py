class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        def bfs(q):
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if(r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == 2147483647):
                       grid[r][c] = grid[row][col] + 1
                       q.append((r, c))
                       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        bfs(q)      
        