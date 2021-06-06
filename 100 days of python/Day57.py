import re as r

string = "The quick brown fox jumps over the lazy dog"
value = r.search("^The.*dog$",string)

if value:
    print("YES--- UwU")
else:
    print("NOO--- -u-")   