import json
import requests
import hmac
import base64
import hashlib
import datetime

KEY="ALTR-8FD0287BD6735CC1812E6C8A041CFD2B"
SECRET="6e8bc5007ef9bcec3c6b55e7c461e34bf2ab0bb7c5f17d10650172dc7fa36a1f"
URL = "https://dgl-hackathon.dev.altr.com/api/v1/chain/"

with open('patient.json','r') as f:
    patientRecords = json.load(f)

url = "https://dgl-hackathon.dev.altr.com/api/v1/chain"

payload = patientRecords

def createHMAC(message, secret):
    secret = secret or ""
    keyBytes = secret.encode('ascii')
    messageBytes = message.encode('ascii')

    digest = hmac.new(keyBytes, msg=messageBytes, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    return str(signature)[2:46]


def generateHMACPayload(method, refToken, dt):
    print(str(dt))
    return str(method) + '\n' + str(refToken) + '\n' + str(dt) + '\n'


date = datetime.datetime.utcnow().isoformat();

AUTH = 'ALTR {}:{}'.format(KEY, createHMAC(generateHMACPayload("POST","", date), SECRET))

headers = {
    'Authorization': AUTH,
    'Content-Type': "application/json",
    'X-ALTR-DATE': date,
    'cache-control': "no-cache",
    'Postman-Token': "c5feac53-462c-4189-b581-ce654360d71e"
    }

response = requests.request("POST", url, data= str(payload) , headers=headers)

print(response.text)
