def solution(prices):
    min_price = max(prices) ## need to set the best[min] buying price, currently setting it to the max price
    max_profit = 0 

    for i in prices: ## for every day price 
        if i < min_price: ## if the price is less than the min price, 
            min_price = i ## set the min price to the current price

        else:
            curr_profit = i - min_price ## else, calculate the profit with the current price and the min price
            max_profit = max(max_profit, curr_profit) ## update the max_profit accordingly

    return max_profit


print(solution([7,1,5,3,6,4]))
print(solution([7,6,4,3,1]))