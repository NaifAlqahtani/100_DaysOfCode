i = str(2.14159)
pi = i.replace("2","3")

print("pi equals to",pi)

string = str(input("Enter text: "))
length = len(string)

if string == string.lower():  #Input a string and returns if its lower or upper case
    print('Lower case! and its length is:',length)
elif string == string.upper():
    print('Upper case! and its length is:',length)
else:
    print('Neither Upper nor Lower but its length is:',length)