
def get_price(prices):

    min_value=prices[0]

    max_value=0

    for i in range(len(prices)):
        price= prices[i]

        if price< min_value:
            min_value=price
        else:
            profet= price - min_value
    
            if profet > max_value:

                 max_value= profet
                 
    return max_value  

print(get_price([4,6,3,5,1,7]))
