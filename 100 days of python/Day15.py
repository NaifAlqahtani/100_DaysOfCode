list1 = ['Blue','Green','Black','Yellow']
list2 = list1.copy()


list2.append('Red')
list1.insert(1, 'White')
list1.remove('Black')
list1.pop()

length1 = len(list1)
length2 = len(list2)

print("{} it's length is {}\n\n{} it's length is {}".format(list1,length1,list2,length2))