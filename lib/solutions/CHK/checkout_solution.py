# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        def get_count(product):
            return skus.count(product)

        if skus.isalpha():
            # initializing price variable
            price = 0
            #defining items dictionary
            dict_products = {
                'A': 50,
                'B': 30,
                'C': 20,
                'D': 15,
                'E': 40
            }
            dict_discount_quantity = {'A': [(5,200), (3,130)], 'B': [(2, 45)]}
            special_discount = {'B': [(2,'E')]}

            unique_items_cart = ''.join(set(skus))
            for elem in unique_items_cart:
                if elem in dict_products:
                    final_price = tmp_price = discount_price = 0
                    cnt_product = get_count(elem)
                    if elem in dict_discount_quantity:
                        discount_price =  int(int(cnt_product / dict_discount_quantity[elem]) * dict_discount_price[elem])
                        no_discount_price = int((cnt_product % dict_discount_quantity[elem]) * dict_products[elem])
                        final_price = discount_price + no_discount_price
                    else:
                        final_price = cnt_product * dict_products[elem]
                    price += int(final_price)
                else:
                    price = -1
                    break
        else:
            price = -1 if skus else 0

        return price

    except Exception as e:
        price = str(e)

    return price


