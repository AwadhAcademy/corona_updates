from datetime import date

import requests

india = requests.get('https://api.covid19india.org/data.json')
india1= india.json()['statewise']
filter1=None
for i in india1:
    if i['state']=='Delhi':
        filter1=i

print(filter1)


# 2021-04-18T00:00:00Z
# 2021-04-18T00:00:00Z
