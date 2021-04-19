import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        extension = file.name.split('.')[1]
        if(extension=="yml" or extension=="yaml"):
              try:
                yaml.safe_load(file.read())
                file.close()
                print("Valid YAML!")
              except:
                print("invalid, Not YAML")
        else:
            print("invalid format, not YAML")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkyaml.py <file>")