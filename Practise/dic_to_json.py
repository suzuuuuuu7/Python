import json
data = {
    "Name":"suja kc",
    "Rollno":33,
    "Marks":[44,39,300,34],
    "Weight":80.8,
}

with open("dicjson.json","w") as file:
    json.dump(data,file,indent=4)