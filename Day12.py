sentence = 'Please, I want {} sandwiches and {} donuts'

string = sentence.replace('I','we') #Step 1

reciept = string.format(5,7) #Step 2

capital = reciept.replace('a','A') #Step 3

print(capital)