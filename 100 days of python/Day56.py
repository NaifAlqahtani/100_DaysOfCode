import json

x = {
    'name': 'Bob',
    'age': 19,
    'Married': False,
    'pets': None
}

print(json.dumps(x, indent=4,separators=(". "," = ")))