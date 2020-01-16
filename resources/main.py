'''
newfile = open("newfile.txt", "w+")

string = "This is the content that will be written in the text file."

newfile.write(string)
'''

import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] +1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Nick", "age": 26}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
