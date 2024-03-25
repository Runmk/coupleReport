import json


def json_process(jsonfile):
    try:
        with open(jsonfile, 'r') as file:
            data = json.load(file)
            formatted_json = json.dumps(data, indent=2)
            print("解析到JSON数据:", formatted_json)
            return data
    except json.JSONDecodeError as e:
        print(f"解析JSON时发生错误:{e}")
