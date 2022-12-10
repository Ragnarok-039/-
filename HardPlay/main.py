import requests as r
import json

from time_stamp import time_stamp
from hash import hash_object

api_key = 'ughJUGY8tygJ0t34phpdfshLgfthgfG'
api_secret = 'LH54dryui2bt4np1qvt4Likoif'

url = 'https://testout.sovcomins.ru/eosago'

# user_request = r'''{ "request_dt": "2001-01-29T17:23:43.998+02:00",
#                  "request_id": "1c2d47d9dfbbeb3fea6a52b3298bb8a20eb25430b71baaaacfd3b2ae42bd6795",
#                  "data": { 9 "vehicleIdent": { "vin": "X4XDM6804X0000246", "licensePlate": "B458KM199" } } }'''

user_request = {"request_dt": "2001-01-29T17:23:43.998+02:00",
                "request_id": "1c2d47d9dfbbeb3fea6a52b3298bb8a20eb25430b71baaaacfd3b2ae42bd6795",
                "data": {"vehicleIdent": {"vin": "X4XDM6804X0000246", "licensePlate": "B458KM199"}}}
user_request_dumps = json.dumps(user_request, sort_keys=True, indent=4)

time_request = time_stamp()

print(type(user_request_dumps))
print(user_request_dumps)
print(json.loads(user_request_dumps))
print(type(json.loads(user_request_dumps)))

print('-' * 30)
hashed_user_request_dumps = hash_object(user_request_dumps)

request_signature = f'{api_key}/{time_request}/{hashed_user_request_dumps}/{api_secret}'
hashed_request_signature = hash_object(request_signature)

print(hashed_user_request_dumps)
print(request_signature)
print(hashed_request_signature)
print('-' * 30)

authorization = f'liberty.insurance-hmac timestamp="<{time_request}>" apikey="<{api_key}>" hmac="<{hashed_request_signature}>"'
authorization = json.dumps(authorization, sort_keys=True, indent=4)
authorization = json.loads(authorization)

params = {'Authorization': 'authorization'}

print(type(authorization))
print(time_request)

now = r.post(url, headers=authorization)
# temp = r.get(f'https://{url}/calculatePolicyCost', timeout=5)

# print(temp.text)
print(now.text)
print('-' * 30)
print(now.headers)
