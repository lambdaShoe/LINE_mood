import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "excited", "chill" ,"sad" ,"little_excited" ,"very_excited",
            "wine", "travel" , "little_sad" , "very_sad" , "Pop" , "HipHop" ,
            "EDM" , "Rock" , "Rap" , "Metal" , "Fusion" , "Classic" , "Jazz" ,
            "Soul","mood","fsm"],
    transitions=[
	{
            "trigger": "advance",
            "source": "*",
            "dest": "mood",
            "conditions": "is_going_to_mood",
        },
	{
            "trigger": "advance",
            "source": "*",
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source": "mood",
            "dest": "excited",
            "conditions": "is_going_to_excited",
        },
        {
            "trigger": "advance",
            "source": "mood",
            "dest": "chill",
            "conditions": "is_going_to_chill",
        },
        {
            "trigger": "advance",
            "source": "mood",
            "dest": "sad",
            "conditions": "is_going_to_sad",
        },
        {
            "trigger": "advance",
            "source": "excited",
            "dest": "little_excited",
            "conditions": "is_going_to_little_excited",
        },
        {
            "trigger": "advance",
            "source": "excited",
            "dest": "very_excited",
            "conditions": "is_going_to_very_excited",
        },
        {
            "trigger": "advance",
            "source": "chill",
            "dest": "wine",
            "conditions": "is_going_to_wine",
        },
        {
            "trigger": "advance",
            "source": "chill",
            "dest": "travel",
            "conditions": "is_going_to_travel",
        },
	{
            "trigger": "advance",
            "source": "sad",
            "dest": "little_sad",
            "conditions": "is_going_to_little_sad",
        },
	{
            "trigger": "advance",
            "source": "sad",
            "dest": "very_sad",
            "conditions": "is_going_to_very_sad",
        },
        {
            "trigger": "advance",
            "source": "little_excited",
            "dest": "Pop",
            "conditions": "is_going_to_Pop",
        },
        {
            "trigger": "advance",
            "source": "little_excited",
            "dest": "HipHop",
            "conditions": "is_going_to_HipHop",
        },
        {
            "trigger": "advance",
            "source": "very_excited",
            "dest": "EDM",
            "conditions": "is_going_to_EDM",
        },
        {
            "trigger": "advance",
            "source": "very_excited",
            "dest": "Rock",
            "conditions": "is_going_to_Rock",
        },
        {
            "trigger": "advance",
            "source": "very_excited",
            "dest": "Rap",
            "conditions": "is_going_to_Rap",
        },
        {
            "trigger": "advance",
            "source": "very_excited",
            "dest": "Metal",
            "conditions": "is_going_to_Metal",
        },
        {
            "trigger": "advance",
            "source": "wine",
            "dest": "Fusion",
            "conditions": "is_going_to_Fusion",
        },
	{
            "trigger": "advance",
            "source": "wine",
            "dest": "Classic",
            "conditions": "is_going_to_Classic",
        },
	{
            "trigger": "advance",
            "source": "wine",
            "dest": "Jazz",
            "conditions": "is_going_to_Jazz",
        },
	{
            "trigger": "advance",
            "source": "wine",
            "dest": "Soul",
            "conditions": "is_going_to_Soul",
        },
       
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine = TocMachine().machine
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
