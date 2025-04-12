import requests
from login import login

headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'text/plain',
    'Referer': 'https://www.fantrax.com/home',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

teamInfoData = {
    "msgs": [{"method": "getStandings", "data": {}}],
    "uiv": 3,
    "refUrl": "https://www.fantrax.com/fantasy/league/5vc0b3b6m1y0gw2l/standings",
    "dt": 0,
    "at": 0,
    "av": "3.0",
    "tz": "America/New_York",
    "v": "163.0.0"
}

params = {'leagueId': '5vc0b3b6m1y0gw2l'}

session = requests.Session()
login(session, headers)


response = session.get('https://www.fantrax.com/fxpa/req', params=params, headers=headers, json=teamInfoData)
response.raise_for_status()
response_json = response.json()

print(response_json)