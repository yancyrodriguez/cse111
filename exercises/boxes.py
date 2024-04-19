import math

items = int(input(f'Enter a number of items:'))
items_box = int(input(f'Enter the number of items per box:'))

boxes = math.ceil(items / items_box)

print(f'for {items} items, packing {items_box} items in each box you will need {boxes}')