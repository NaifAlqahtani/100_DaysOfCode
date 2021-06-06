import re as r

string = "data is the new oil"
x = r.search(r"\b(\w*data\w*)\b",string)
print(x,"\n",x.group())
