import sys

class Solution():
    def cal_num_of_path(self) -> int:
        self.n, self.m = list(map(int, sys.stdin.readline().strip().split()))
        self.heights = []
        for _ in range(self.n):
            self.heights.append(list(map(int, sys.stdin.readline().strip().split())))

        self.x, self.y, self.z, self.w = list(map(int, sys.stdin.readline().strip().split()))

        self.count = 0

        self.directs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        def dfs(now_x: int, now_y: int):
            print(now_x, now_y)
            if now_x == self.z and now_y == self.w:
                self.count += 1
                return
            if self.heights[now_x][now_y] >= self.heights[self.z][self.w]:
                return
            for direct in self.directs:
                next_x = now_x + direct[0]
                next_y = now_y + direct[1]
                if next_x < self.n and next_y < self.m and self.heights[now_x][now_y] < self.heights[next_x][next_y]:
                    dfs(next_x, next_y)
        start_x, start_y = self.x, self.y
        dfs(start_x, start_y)
        # print(self.count)
        return self.count

s = Solution()
print(s.cal_num_of_path())

