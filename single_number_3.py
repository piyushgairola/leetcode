class Solution:
    def single_number(self, nums):
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1

        _dic = dict(sorted(dic.items(), key=lambda item: item[1])[:2])
        res = list(_dic.keys())
        return res


if __name__ == "__main__":
    obj = Solution()
    ls = [1,2,3,1,2,1,5]
    print(obj.single_number(ls))