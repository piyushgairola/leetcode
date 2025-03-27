def suggestedProducts(products,searchWord):
    products.sort()
    n = len(products)
    prefix = ""
    ans = []
    for c in searchWord:
        temp = []
        prefix += c
        prod_idx = binarySearch(products, prefix)

        # for i in range(prod_idx, min(n,prod_idx+3)):
        #     temp.append(products[i])

        ans.append([products[i] for i in range(prod_idx, min(n,prod_idx+3)) if products[i].startswith(prefix)])

    return ans

def binarySearch(products,prefix):
    low = 0
    high = len(products)

    while low<high:
        mid = (low+high)//2
        if products[mid]<prefix:
            low = mid+1
        else:
            high = mid

    return low


if __name__ == "__main__":
    products = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"

    print(suggestedProducts(products,searchWord))