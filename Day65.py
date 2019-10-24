price = 49
quantity = 3
total = price*quantity
string = 'You have purchased {} tomatos each costing ${:.2f} all totalling to ${:.2f}'
print(string.format(quantity, price, total))