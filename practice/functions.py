def apply_discount(price,discount):
    if not isinstance(price,(int,float)):
        print('The price should be a number')
    elif price <= 0:
            print('The price should be greater than 0')
    elif not isinstance(discount,(int,float)):
        print('The discount should be a number')
    elif discount < 0 or discount > 100:
            print('The discount should be between 0 and 100')
    
    else:
        print(price - (price * (discount/100)))

apply_discount(100,3)