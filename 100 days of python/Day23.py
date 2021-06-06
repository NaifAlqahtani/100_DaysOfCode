dictionary = {
    "University": "KFUPM",
    "Year Joined": '2019',
    "Student ID": '2019314159'
}
itemLookedFor = "Student ID"

if  itemLookedFor in dictionary:
    print(itemLookedFor,"is present")

print("Length of this dictionary is",len(dictionary))

dictionary["Course"] = "Computer Science"

for i,j in dictionary.items():
    print(i,': ',j)