import json
import requests
from datetime import datetime, timedelta
from json_process import json_process
from dateutil import parser

if __name__ == '__main__':
    json_file = "massageConfig.json"
    jsonData = json_process(json_file)

    API_KEY = jsonData['app_id']
    USER_ACCOUNT = jsonData['user']
    TEMPLATE_ID = jsonData['template_id']
    APP_SECRET = jsonData['app_secret']
    APP_ID = jsonData['app_id']
    WEATHER_KEY = jsonData['weather_key']
    print("APP_ID =", APP_ID, "APP_SECRET =", APP_SECRET)
    url = f"https://devapi.qweather.com/v7/weather/3d?location=116.66,39.88&key={WEATHER_KEY}"
    token_url = (f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}"
                 f"&secret={APP_SECRET}")

    response = requests.get(url)
    access_token = requests.get(token_url).json()['access_token']

    print(access_token)

    data = response.json()
    weather_update = data['updateTime']
    textDay = data['daily'][1]['textDay']
    windDirDay = data['daily'][1]['windDirDay']

    tempMax = data['daily'][1]['tempMax']
    tempMin = data['daily'][1]['tempMin']
    sunrise = data['daily'][1]['sunrise']
    sunset = data['daily'][1]['sunset']

    print(weather_update, textDay, windDirDay, tempMin, tempMax, sunrise, sunset)
