list1 = ['apple','banana']
list2 = ['red','yellow']

valueOflist1 = "banana" not in list1
valueOflist2 = list1 is list2

print(valueOflist1,valueOflist2)

if valueOflist1 == valueOflist2 == True:
    print("Both values are True")
elif valueOflist1 != valueOflist2:
    print("only 1 of the values is True")
else:
    print("Both values are False")