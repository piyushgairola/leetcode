import heapq
class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        pq = [(grid[0][0],0,0)]
        ans = 0
        seen = set([(0,0)])

        while True:
            T,x,y = heapq.heappop(pq)
            ans = max(ans,T)

            if x==y==n-1:
                return ans

            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=i<n and 0<=j<n and (i,j) not in seen:
                    seen.add((i,j))
                    heapq.heappush(pq,(grid[i][j],i,j))


if __name__ == "__main__":
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

    obj = Solution()
    print(obj.swimInWater(grid))
