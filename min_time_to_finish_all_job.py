class Solution:
    def minTimeReq(self, jobs, k):
        n_jobs = len(jobs)
        jobs.sort(reverse=True)
        self.worker = [0]*k
        self.ans = sum(jobs)

        def dfs(idx):
            if idx == n_jobs:
                self.ans = min(self.ans, max(self.worker))
                return

            for w_idx in range(k):
                if self.worker[w_idx] + jobs[idx] < self.ans:
                    self.worker[w_idx] += jobs[idx]

                    dfs(idx+1)

                    self.worker[w_idx] -= jobs[idx]

                    
                """
I think if count[j] == 0, then from count[j+1] to count[k-1] are all 0
we are trying to find result from index 0 to index k-1, if we didn't put anything on index j, then nothing from j+1 to k-1.
Also if two indexes with same count, such as 0, then they will get same result.
                """
                if self.worker[w_idx] == 0:
                    break

            return False

        dfs(0)
        return self.ans


if __name__ == "__main__":
    obj = Solution()
    jobs = [3, 2, 3]
    k = 3
    print(obj.minTimeReq(jobs, k))
