import re as r

string = "The rain in Spain"
word = r.search(r"\bS\w+",string) #search string for word that begins with capital S

span = word.span() #prints the character span
group = word.group() #prints the word

print(span,"\n",group)