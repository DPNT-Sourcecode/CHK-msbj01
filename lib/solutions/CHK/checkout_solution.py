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
                'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35,
                'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
                'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
            }
            dict_discount_quantity = {'A': [(5,200), (3,130)], 'B': [(2, 45)], 'F': [(3,20)], 'H': [(10, 80), (5, 45)],
                                      'K': [(2, 150)], 'M': [(1, 15)], 'P': [(5, 200)], 'Q': [(3, 80)], 'U': [(4, 120)], 'V': [(3, 130), (2, 90)]}
            special_discount = {'B': [(2,'E')], 'M': [(3, 'N')], 'Q': [(3, 'R')]}

            unique_items_cart = ''.join(set(skus))
            for elem in unique_items_cart:
                if elem in dict_products:
                    final_price = tmp_price = discount_price = 0
                    cnt_product = get_count(elem)
                    if elem in dict_discount_quantity:
                        for val in dict_discount_quantity[elem]:
                            if elem in special_discount:
                                for sdval in special_discount[elem]:
                                    if sdval[1] in unique_items_cart:
                                        cnt_discount = get_count(sdval[1])
                                        if cnt_product > cnt_discount and cnt_product %cnt_discount == 0:
                                            cnt_product = 0
                                        else:
                                            x = int(cnt_discount / sdval[0])
                                            cnt_product-=x
                                    else:
                                        break
                            tmp_price = int(int(cnt_product / val[0]) * val[1])
                            cnt_product = cnt_product % val[0]
                            discount_price += tmp_price
                            no_discount_price = int(cnt_product * dict_products[elem])
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

cart = 'AAAAAAAABBBCCCDDDDEEEEEFFFFFGGGGGHHHHHHHHHHHHIIIJJJJKKKKKLLLMMMMMMNNNNNOOOOPPPPPQQQQRRRRRSSSTTTTUUUUUVVVVVWWWWWXXXXXYYYYYZZZZZ'
#cart = 'MMMMMMNNNNN'
prc = checkout(cart)
print(prc)

# {"method":"checkout","params":["NNNM"],"id":"CHK_R4_106"}, expected: 120, got: 135
#  {"method":"checkout","params":["NNNNM"],"id":"CHK_R4_107"}, expected: 160, got: 175
#  {"method":"checkout","params":["NNNNNNMM"],"id":"CHK_R4_108"}, expected: 240, got: 270




