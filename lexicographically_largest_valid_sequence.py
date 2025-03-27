class Solution:
    def constructDistancedSequence(self,n):
        def dfs(idx):
            if idx == self.m:
                return all(self.ans)            ## return true if all elements are true
            
            if self.ans[idx]:
                return dfs(idx+1)

            for x in range(n,0,-1):
                j = idx if x==1 else idx+x

                if j<self.m and not self.ans[j] and not self.visited[x]:
                    self.ans[idx], self.ans[j] = x, x
                    self.visited[x] = True

                    if dfs(idx+1):
                        return True
                    self.ans[idx], self.ans[j] = 0,0
                    self.visited[x] = False

            return False

        self.m = 2*n-1
        self.ans = [0]*self.m
        self.visited = [False]*(n+1)

        dfs(0)

        return self.ans



if __name__ == "__main__":
    obj = Solution()
    print(obj.constructDistancedSequence(3  ))