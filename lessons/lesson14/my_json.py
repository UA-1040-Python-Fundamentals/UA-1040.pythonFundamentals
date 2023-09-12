import json
x = '{ "name":"Liubov", "age":25, "city":"Lviv"}'
d = json.loads(x)
print(d)
print(d.get("name"))

with open("in/data.json") as file:
    data = json.loads(file.read())


from pprint import pprint
pprint(data, depth=5)
data["set"] = {1,2,3,4}
with open("out/o.json", "w") as file:
    file.write(json.dumps(data))
    print(json.dumps(data))
