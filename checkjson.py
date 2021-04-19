import os
import sys
import json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        extension = file.name.split('.')[1]
        if(extension=="json"):
            try:
                json.load(file)
                file.close()
                print("Valid JSON!")
            except:
                print("invalid, Not JSON")

        else:
            print("invalid format, not JSON")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkjson.py <file>")