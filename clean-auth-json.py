#!/usr/bin/env python
import json
import sys
j = json.load(sys.stdin)
for item in j:
    if item['model'] == 'auth.user':
        del item['fields']['date_joined']
        del item['fields']['last_login']
print json.dumps(j)