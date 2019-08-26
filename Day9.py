names = ["Naif","Mohammed","Ali","Abdullah"]
ages = [19,23,46,12]


for i in range(0,len(names)):
    text = "My name is {0} and I am {1} years old"
    print(text.format(names[i],ages[i]))