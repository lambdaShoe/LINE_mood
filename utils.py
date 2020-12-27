import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

"""
def send_fsm(reply_token):
    line_bot_api.reply_message(
        reply_token,
        ImageSendMessage(
            original_content_url="https://lh3.googleusercontent.com/pw/ACtC-3dv0dTn-45EryPyNIWrarZAj0aD35QyV0CPNu1nTkQP1tdY5q8EvpGFuJFegz9Pkr0Le8pe6p2kNcXvHwLPAlOVJ1YvnuTlAeZoSGTwb50NGKfksvFIiYalFEEfBCssWHwDFYIl5xC_3cQn_4Ls0GE=w2258-h772-no?authuser=2",
            preview_image_url="https://lh3.googleusercontent.com/pw/ACtC-3dv0dTn-45EryPyNIWrarZAj0aD35QyV0CPNu1nTkQP1tdY5q8EvpGFuJFegz9Pkr0Le8pe6p2kNcXvHwLPAlOVJ1YvnuTlAeZoSGTwb50NGKfksvFIiYalFEEfBCssWHwDFYIl5xC_3cQn_4Ls0GE=w2258-h772-no?authuser=2",
            quick_reply=QuickReply(items=[QuickReplyButton(action = MessageAction(label='回到「選單」', text='選單'))])
            )
        )
    return "OK"


def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
