# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        if skus.isalpha():
            # initializing price variable
            price = 0
            #defining items dictionary
            dict_products = {
                'A': 50,
                'B': 30,
                'C': 20,
                'D': 15
            }
            dict_discount_quantity = {'A': 3, 'B': 2}
            dict_discount_price = {'A': 130, 'B': 45}

            unique_items_cart = ''.join(set(skus))
            for elem in unique_items_cart:
                if elem in dict_products:
                    final_price = 0
                    cnt_product = skus.count(elem)
                    if elem in dict_discount_quantity:
                        x = int(cnt_product / dict_discount_quantity[elem])
                        discount_price =  int(x * dict_discount_price[elem])
                        no_discount_price = int((cnt_product % dict_discount_quantity[elem]) * dict_products[elem])
                        final_price = discount_price + no_discount_price
                    else:
                        final_price = cnt_product * dict_products[elem]
                    price += int(final_price)
                else:
                    price = -1
                    break
        else:
            price = -1

        return price

    except Exception as e:
        price = str(e)

    return price

total_price = checkout('AAAAAAAAAABBBBBCCCDDDD')
print (total_price)
