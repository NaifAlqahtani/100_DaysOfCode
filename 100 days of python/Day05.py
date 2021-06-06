x= "apple"
y = "orange"
z= "lemon"

basket = x + y + z


for i in range(0,len(basket),5): 
    print(basket[i:i+5], end = ' ')  #I tried to split the string every 5 letters, unfortunatly orange 
                                     #is 6 letters so the output will be:
                                     # >>>> apple orang elemo n
                                     #
                                     #if orange was replaced with 'grape', the output will be:
                                     # >>>> apple grape lemon
                        
                        
#an easier way to do this correctly will be as follows:
"""
x= "apple"
y = "orange"
z= "lemon"

print(x,y,z)
"""
