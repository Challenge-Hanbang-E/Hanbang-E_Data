import json
import sys
import requests
from dotenv import load_dotenv
import os

load_dotenv()
WEB_HOOK_URL = os.environ.get('WEBHOOK')


def send_slack_msg(title, msg):
    url = WEB_HOOK_URL
    slack_data = {
        "username": "New Data Crawling Bot", # 보내는 사람 이름
        "icon_emoji": ":satellite:",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": msg,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
