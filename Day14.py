import random

fruits = ['Banana', 'Apple', 'Kiwi']
vegtables = ['Broccli', 'Tomato', 'Eggplant']

for i in range(3):
    Basket = fruits + vegtables
    item = random.randint(0,3)

    itemPicked = Basket[item]

    if itemPicked in fruits:
        print('The item picked ({}) is a fruit!'.format(itemPicked))
    elif itemPicked in vegtables:
        print('The item picked ({}) is a vegtable!'.format(itemPicked))

