import json
import requests
from datetime import datetime, timedelta
from json_process import json_process
from dateutil import parser

if __name__ == '__main__':
    json_file = "massageConfig.json"
    jsonData = json_process(json_file)

    API_KEY = jsonData['app_id']
    USER_ACCOUNT = jsonData['user'][0]
    TEMPLATE_ID = jsonData['template_id']
    APP_SECRET = jsonData['app_secret']
    APP_ID = jsonData['app_id']
    WEATHER_KEY = jsonData['weather_key']
    print("APP_ID =", APP_ID, "APP_SECRET =", APP_SECRET,"USER_ACCOUNT =",USER_ACCOUNT)
    url = f"https://devapi.qweather.com/v7/weather/3d?location=116.66,39.88&key={WEATHER_KEY}"
    token_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}"
                 "&secret={}")

    response = requests.get(url)

    data = response.json()
    weather_update = data['updateTime']
    textDay = data['daily'][1]['textDay']
    windDirDay = data['daily'][1]['windDirDay']
    location = "北京市通州区梨园"

    tempMax = data['daily'][1]['tempMax']
    tempMin = data['daily'][1]['tempMin']
    sunrise = data['daily'][1]['sunrise']
    sunset = data['daily'][1]['sunset']

    print(weather_update, textDay, windDirDay, tempMin, tempMax, sunrise, sunset)
    TEMPLATE_SEND_URL = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}"
    response_token = requests.get(token_url.format(APP_ID, APP_SECRET))
    result_token = response_token.json()
    access_token = result_token.get('access_token')

    # 准备模板消息的数据
    datas = {
        "touser": USER_ACCOUNT,
        "template_id": TEMPLATE_ID,
        "url": "https://m.baidu.com/sf?pd=life_compare_weather&openapi=1&dspName=iphone&from_sf=1&resource_id=4982&oe=utf8&alr=1&multiDayWeather=1&title=40天天气预报&query=北京天气",
        "topcolor": "#FF0000",
        "data": {
            "keyword1": {
                "value": "2014年9月22日",
                "color": "#173177"
            },
            "keyword2": {
                "value":  "巧克力",
                "color": "#173177"
            },
            "date": {
                "value": weather_update,
                "color": "#173177"
            },
            "textDay": {
                "value": textDay,
                "color": "#173177"
            },
            "location": {
                "value": location,
                "color": "#173177"
            },
            "tempMin": {
                "value": tempMin,
                "color": "#173177"
            },
            "tempMax": {
                "value": tempMax,
                "color": "#173177"
            },
            "sunrise": {
                "value": sunrise,
                "color": "#173177"
            },
            "sunset": {
                "value": sunset,
                "color": "#173177"
            }
        }
    }

    headers = {'Content-Type': 'application/json'}
    response_template = requests.post(TEMPLATE_SEND_URL.format(access_token), data=json.dumps(datas), headers=headers)

    print(response_template.text)

    if response_template.status_code == 200:
        result = response_template.json()
        if result.get('errcode') == 0:
            print("模板消息发送成功")
        else:
            print(f"发送失败，错误码：{result.get('errcode')}，错误信息：{result.get('errmsg')}")
    else:
        print("请求失败")
