import numpy as np
import requests
import json

cmp = np.load("companies-in-CH.npy")
user_key="user_key=ddb23760741957629a8383611082c258"

#start = 4000
#fin = 4001

for i in range(start,fin):
    rsp = requests.request("GET", cmp[i,1]+"?"+user_key)
    js = json.loads(rsp.text)
    props = js['data']['properties']
    info = dict()
    info['name'] = cmp[i,0]
    info['url'] = cmp[i,1]
    info['founded_on'] = props['founded_on']
    info['num_employees_min'] = props['num_employees_min']
    info['num_employees_max'] = props['num_employees_max']
    info['rank'] = props['rank']
    info['description'] = props['description']
    info['short_description'] = props['short_description']
    info['total_funding_usd'] = props['total_funding_usd']
    cmp_new.append(info)
    print("currently: "+str(i))

import json
with open('list-'+str(start)+'-'+str(fin)+'.json', 'w') as fp:
    json.dump(cmp_new, fp)

