import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
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
        print (skus)
        lst_cart = skus.split(',')
        for elem in lst_cart:
            final_price = 0
            extract_num = re.findall('\d+', elem)
            cnt_product = int(extract_num[0])
            extract_str = elem.replace(extract_num[0],'')

            if extract_str in dict_discount_quantity:
                x = int(cnt_product / dict_discount_quantity[extract_str])
                discount_price =  x * dict_discount_price[extract_str]
                no_discount_price = (cnt_product % dict_discount_quantity[extract_str]) * dict_products[extract_str]
                final_price = discount_price + no_discount_price
            else:
                final_price = cnt_product * dict_products[extract_str]

            price += int(final_price)
    except Exception as e:
        price = str(e)

    return price

