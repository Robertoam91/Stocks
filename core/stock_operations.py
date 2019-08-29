from core.utils import number_operations

def most_profit(stock_price_list):
    """
    Given a list of stock prices sorted by date, this function will find two values.
    First value will be the "buy" value.
    Second value will be the "sell" value.
    Given values are optimized for maximum profit.
    :param stock_price_list: List of stock prices.
    :return: List
    """
    #Run in O(n)
    max_price, max_index = number_operations.get_maximum_value(stock_price_list)
    # Run in O(n)
    min_price, min_index = number_operations.get_minimum_value(stock_price_list)
    min_dif = [0, max_price]
    # Replaced old implementation of list.index(max) > list.index(min), we were running two O(n) operations more
    if max_index > min_index:
        # If we got it at the first try, return the indices
        return min_price, max_price
    # Else, start going through the list to search the minimum difference between the actual minimum number
    # that comes before our identified maximum number
    for index in range(stock_price_list.index(max_price) - 1):
        if stock_price_list[index] - min_price < min_dif[1]:
            min_dif[0] = index
            min_dif[1] = stock_price_list[index] - min_price
    # Finally, return the minimum price and the maximum price
    return stock_price_list[min_dif[0]], max_price