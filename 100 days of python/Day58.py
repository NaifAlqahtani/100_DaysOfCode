import re as r

str = "The rain in Spain"



value = r.findall('ai', str)
print(value)
'----------------------------'
value1 = r.search(' ', str)
print(value1.start())
'----------------------------'
value2 = r.split(' ', str)
print(value2)