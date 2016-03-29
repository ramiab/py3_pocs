# https://www.interviewcake.com/question/python/stock-price

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# stock_prices_yesterday = [10, 7, 6, 2, 1]

def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for current_price in stock_prices_yesterday[1:]:

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)


    return max_profit


print( get_max_profit(stock_prices_yesterday) )
# returns 6 (buying for $5 and selling for $11)