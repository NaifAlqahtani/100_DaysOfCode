import json

#convert pyton to json 
x = {"name": "naif"}

y = json.dumps(x)
print(y)

#convert json to pyton
n = '{"name": "naif"}'
m = json.loads(n)
print(m["name"])