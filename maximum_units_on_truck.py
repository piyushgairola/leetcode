def maxUnits(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key= lambda x: x[1], reverse=True)
    ans = 0

    for box, unit in boxTypes:
        if truckSize >0:
            if truckSize >= box:
                ans += box*unit
                truckSize -= box

            else:
                ans += truckSize*unit
                break

    return ans



boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(maxUnits(boxTypes, truckSize))
            

        