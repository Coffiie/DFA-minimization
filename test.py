import json

list = [{'b': 's1', 'a': 's2'}, {'a': 's3', 'b': 's1'}, {'c': 's3'}]
states = ["s1","s2","s3"]
dict = {}
count =0
for item in list:
    dict[states[count]]= item
    count+=1
print(dict)