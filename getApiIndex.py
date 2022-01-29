import requests
import json

url = 'https://frc-api.firstinspires.org/v2.0/:season'

payload={}
headers = {
  'Authorization': 'Basic <credentials>',
  'If-Modified-Since': ''
}
response = requests.get(url).text
response_info = json.loads(response)

'''requests.get('https://frc-api.firstinspires.org/v2.0/:season').json()'''
print(response)
