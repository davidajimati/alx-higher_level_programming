#!/usr/bin/python3
'''
This module adds all arguments (from the command line)
to a Python list, and then save them to a file:
'''

# Import all that is needed
import json, sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# what if the file doesn't exist before?
# Function Check if the JSON file is empty Returns True if empty


filename = "add_item.json"
content = []
try:
    # with open(filename, 'r') as fl:
    #     check = json.load(fl)

    if len(sys.argv) > 0:
        # Loop through it and append the str. of each argument
        for i in range(1, len(sys.argv)):
            content.append(str(sys.argv[i]))
        print(content)
        print("I worked")

        # Create open the json file and add dump the new list into it
        with open(filename, 'a') as f:
            # Load the content of the json file
            exist = load_from_json_file(filename)
            # Adding the list to it
            exist += content
            # Saving it back to the json file
            save_to_json_file(exist, filename)
    else:
        sys.exit

except Exception:
    init = []
    with open(filename, 'w') as new_json:
        json.dump(init, new_json)
