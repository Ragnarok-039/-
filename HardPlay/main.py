import requests as r
import json

from time_stamp import time_stamp
from request_signature import request_signature

api_key = 'ughJUGY8tygJ0t34phpdfshLgfthgfG'
api_secret = 'LH54dryui2bt4np1qvt4Likoif'

url = 'https://testout.sovcomins.ru/eosago'

user_request = {"request_dt": "2001-01-29T17:23:43.998+02:00",
                "request_id": "1c2d47d9dfbbeb3fea6a52b3298bb8a20eb25430b71baaaacfd3b2ae42bd6795",
                "data": {"vehicleIdent": {"vin": "X4XDM6804X0000246", "licensePlate": "B458KM199"}}}
user_request_dumps = json.dumps(user_request, sort_keys=True, indent=4)

time_request = time_stamp()

hashed_request_signature = request_signature(user_request_dumps, api_key, time_request, api_secret)

authorization = f'''liberty.insurance-hmac 
                    timestamp="<{time_request}>" 
                    apikey="<{api_key}>" 
                    hmac="<{hashed_request_signature}>"'''
authorization = json.dumps(authorization, sort_keys=True, indent=4)

params = {'Authorization': 'authorization'}

now = r.post(url, headers=authorization)
print(now.text)
