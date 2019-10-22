import json

rPath = "/Users/ddesai/dd/python/Python/PY_TEST/JSON/newrelic.json"

# Read File (File context is in YAML format)
cValue = open(rPath, "r")
fRead = cValue.read()
cValue.close()

val = json.loads(fRead)
print ("Image Tag (JSON): {}".format(val["applications"][0]["id"]))