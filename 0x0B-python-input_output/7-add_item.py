#!/usr/bin/python3
'''
This module adds all arguments (from the command line)
to a Python list, and then save them to a file:
'''

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
with open(filename, 'a') as f:
    exist = load_from_json_file(filename)

cnt = 1
# if exist:
while (cnt <= len(sys.argv)):
    exist.append(sys.argv[cnt])
    cnt += 1
save_to_json_file(exist, filename)

# else:
#     content = []
#     cnt = 1
#     with open(filename, 'a') as file:
#         while (cnt <= len(sys.argv)):
#             content.append(sys.argv[cnt])
#             cnt += 1
#         save_to_json_file(content, filename)
