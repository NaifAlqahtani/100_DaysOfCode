print('Hello world! "this is a text with quotes"') #you can use double quotes inside a text when the outer text is single quotes. this can be helpful to display a quote line in terminal!

string = "Foobar"

print(string[-1:]) #prints the last letter of the string
print(string[:-1],"\n") #prints all letters except last letter

for i in range(0,len(string)):
    print(string[i]) #prints each letter on a seprate line
