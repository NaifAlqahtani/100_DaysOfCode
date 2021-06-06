dictionary = {
    'Brand': 'Apple',
    'Model': 'Macbook Pro',
    'PYear': '2012'
}
update = dictionary["PYear"] = '2019'

for i in dictionary:
    print("{}:............{}".format(i, dictionary[i]))

print('---------------------------------')

for i,j in dictionary.items():
    print(i+':............'+j)