import itertools
import sys

item_price_list = [0.56, 0.56, 0.56, 0.56, 1.75, 0.75, 0.99, 2.51]
target_price = 5
error = 0.1
print('%10s %40s ||  %10s %s' % ('Bought', 'items', 'not Bought', 'items'))
for i in range(1, len(item_price_list) + 1):
    for pos in itertools.combinations(item_price_list, i):
        total = sum(pos)
        if abs(total - target_price) < error:
            bought_items = pos
            not_bought_items = [a for a in item_price_list if a not in pos]
            total_not_bought = sum(not_bought_items)

            print('%10.4s %40s ||  %10.4s %s' % (total, bought_items, total_not_bought, not_bought_items))
