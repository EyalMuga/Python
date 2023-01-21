import requests
import base64


def to_base64(s):
    return base64.b64encode(s.encode('utf-8'))


print(to_base64('url-path'))

url = "https://www.virustotal.com/api/v3/urls"

headers = {
    'accept': "application/json",
    'content-type': "application/x-www-form-urlencoded",
    'x-apikey': ""
}
