#!/usr/bin/env python3

import os
import json 

print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))
# print(json.dumps(dict(os.environ.get('QUERY_STRING')), indent=2))