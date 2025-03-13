import requests

slack_token = ""

class Slack:
    def __init__(self, _msg):
        response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer " + slack_token},
            data={"channel": "#upbit","text": _msg}
        )