import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_fsm(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(
        reply_token,
        ImageSendMessage(
            original_content_url="https://lh3.googleusercontent.com/pw/ACtC-3eo0JiMOJAVzeHmjFPTTEHzP53I-tyn939RR4hIBHoUtgfrURKexLv3OSoui1rpNWcv9gpUG0KNnetC3aJ7dpikaAoZuJ1A27nkfk4S5gp_f2iFCZmGJfH1N9ia4BkgvdIDdZg1hy7FRt4YJlRplvI=w1423-h943-no?authuser=0",
            preview_image_url="https://lh3.googleusercontent.com/pw/ACtC-3eo0JiMOJAVzeHmjFPTTEHzP53I-tyn939RR4hIBHoUtgfrURKexLv3OSoui1rpNWcv9gpUG0KNnetC3aJ7dpikaAoZuJ1A27nkfk4S5gp_f2iFCZmGJfH1N9ia4BkgvdIDdZg1hy7FRt4YJlRplvI=w1423-h943-no?authuser=0"
            )
        )
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
