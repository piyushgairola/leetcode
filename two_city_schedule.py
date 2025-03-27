class Solution:
    def twoCitySchedCost(self, costs):
        diff_cost = list()
        total_cost = 0
        for cost in costs:
            diff_cost.append(cost[0] - cost[1])

        print(diff_cost)
        sort_diff_cost = sorted(diff_cost)
        total_candidate = len(costs)
        print(sort_diff_cost)
        for i in range(total_candidate):
            idx = diff_cost.index(sort_diff_cost[i])
            if i < total_candidate // 2:
                total_cost += costs[idx][0]
            else:
                total_cost += costs[idx][1]

        return total_cost


if __name__ == '__main__':
    costs = [[945, 563], [598, 753], [558, 341], [372, 54], [39, 522], [249, 459], [536, 264], [491, 125], [367, 118],
             [34, 665], [472, 410], [109, 995], [147, 436], [814, 112], [45, 545], [561, 308], [491, 504], [113, 548],
             [626, 104], [556, 206], [538, 592], [250, 460], [718, 134], [809, 221], [893, 641], [404, 964], [980, 751],
             [111, 935]]
    obj = Solution()
    print(obj.twoCitySchedCost(costs))
