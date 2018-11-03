import requests
import json
import hmac
import base64
import hashlib
import datetime
import ast

KEY="ALTR-8FD0287BD6735CC1812E6C8A041CFD2B"
SECRET="6e8bc5007ef9bcec3c6b55e7c461e34bf2ab0bb7c5f17d10650172dc7fa36a1f"
REF = "chain_c7058d7bb0ad4645d7032d7668b82ba4e2f9cc88f1ffaf5c209c523d2037fa9a"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain/"


def createHMAC(message, secret):
    secret = secret or ""
    keyBytes = secret.encode('ascii')
    messageBytes = message.encode('ascii')

    digest = hmac.new(keyBytes, msg=messageBytes, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature

def generateHMACPayload(method, refToken, dt):
    print(str(dt))
    return str(method) + '\n' + str(refToken) + '\n' + str(dt) + '\n'


date = datetime.datetime.utcnow().isoformat();

AUTH = 'ALTR {}:{}'.format(KEY, createHMAC(generateHMACPayload("GET", REF, date), SECRET))

#
headers = {
    'Authorization': AUTH,
    'Content-Type': "application/json",
    'X-ALTR-DATE': date,
    'cache-control': "no-cache"
    }
#
response = requests.request("GET", URL + REF, headers=headers)

with open("blockChainResponse.json","w") as fp:
    json.dump(ast.literal_eval(response.text), fp, indent = 4)

print(response.text)
print ("done")
