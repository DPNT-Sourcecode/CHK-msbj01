import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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

    lst_cart = skus.split(',')
    for elem in lst_cart:
        final_price = 0
        extract_num = re.findall('\d+', elem)
        cnt_product = int(extract_num[0])
        extract_str = elem.replace(extract_num[0],'')

        if extract_str in dict_discount_quantity:
            discount_price = (cnt_product / dict_discount_quantity[extract_str]) * dict_discount_price[extract_str]
            no_discount_price = (cnt_product % dict_discount_quantity[extract_str]) * dict_discount_price[extract_str]
            final_price = discount_price + no_discount_price
        else:
            final_price = cnt_product * dict_products[extract_str]

        price += int(final_price)

    print (price)


checkout('50A,30B,40C')


