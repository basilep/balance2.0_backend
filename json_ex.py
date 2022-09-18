import json
list_json = {"message":  "souye"}
list_json.update({"freq": 5})
list_json.update({"permanent": False})
json_ex = json.dumps(list_json)
print(json_ex)