import requests
import urllib3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "91142",
    'client_secret': '7884fdc10ff8cfd276b4742fb189657e7769d770',
    'refresh_token': 'a724bf6544b3865d659f8c16fce7f5cf3ae3ef5a',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()
activities = pd.json_normalize(my_dataset)

print(my_dataset[1]["name"])
print(my_dataset[0]["map"]["summary_polyline"])