def maxArea(h,w,horizontalCuts,verticalCuts):
    def getBlocks(n, cuts):
        t = 0
        blocks = []
        for i in cuts:
            blocks.append(i-t)
            t=i

        if t!=n:
            blocks.append(n-t)

        return blocks
    horizontalCuts.sort()
    verticalCuts.sort()
    h_blocks = getBlocks(h,horizontalCuts)
    v_blocks = getBlocks(w,verticalCuts)

    return max(h_blocks)*max(v_blocks)%1000000007


if __name__ == "__main__":
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    print(maxArea(h,w,horizontalCuts,verticalCuts))
