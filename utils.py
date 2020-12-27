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
            original_content_url="https://lh3.googleusercontent.com/a3Jq3uXkYONmdUr3JDum1r_pTerMclSbD4J_-EMPNWq_vM5h6Y1Ai80XeeUaaHsoeZ6K5PBP3ZgcE3cDMFGgHqu9CvX5p8DTKMyU7YLKyHU30lwazspTrGXnWrLhAQ0plQjgB0hL9aEikghdmq_74nSydtOwp-WTmauKezaxdToOmbFn7-E-bfO582rrOnNCRnAKnylIv_UzheIcScpAQKCiVRq9W3fp_ENA6eUJmHDVfj1uFHVMksT3O9mQh21r-lKvdNTORoDJvk4wCzH02lnEdv0wKB1udPh4e1hZ3p1wVygjGrVZhr2BXlbTBUdkqJf-2qMiQrNauPgxypDM8nPcJE59Y5jx4hp6EHkcMoMtpVK9n53C4ht6Bkf5dwW2FPbhH6MGU8Hw6ueGweOPzj8-V1JbvnNFLcwr5J-vHpUST-Ycf5gLm5qAJC-dV-7eNkDJ57DdLsRieMfdOj0Wcmdpna_53lEAO3FbruqURDmglbyfzKykrK_WeXFI4HIDFGJevts6hTpa0VqymbnN-_JSOexwa1SNo-7927TSU9zopv2HszRdsJ3_Etu94OWyT8nwa5zgkU8E44shAp27t88ptB2Jx_ZQN_EAjL_fcf6TDev7J6PpVlnI6MmZ7xh7_-Lyl4FXi80XBBqaQDo4d55Zi1xfohtsPs1iokDQNXQWyqjRoIJdcMvWLYXn=w1423-h943-no?authuser=0",
            preview_image_url="https://lh3.googleusercontent.com/a3Jq3uXkYONmdUr3JDum1r_pTerMclSbD4J_-EMPNWq_vM5h6Y1Ai80XeeUaaHsoeZ6K5PBP3ZgcE3cDMFGgHqu9CvX5p8DTKMyU7YLKyHU30lwazspTrGXnWrLhAQ0plQjgB0hL9aEikghdmq_74nSydtOwp-WTmauKezaxdToOmbFn7-E-bfO582rrOnNCRnAKnylIv_UzheIcScpAQKCiVRq9W3fp_ENA6eUJmHDVfj1uFHVMksT3O9mQh21r-lKvdNTORoDJvk4wCzH02lnEdv0wKB1udPh4e1hZ3p1wVygjGrVZhr2BXlbTBUdkqJf-2qMiQrNauPgxypDM8nPcJE59Y5jx4hp6EHkcMoMtpVK9n53C4ht6Bkf5dwW2FPbhH6MGU8Hw6ueGweOPzj8-V1JbvnNFLcwr5J-vHpUST-Ycf5gLm5qAJC-dV-7eNkDJ57DdLsRieMfdOj0Wcmdpna_53lEAO3FbruqURDmglbyfzKykrK_WeXFI4HIDFGJevts6hTpa0VqymbnN-_JSOexwa1SNo-7927TSU9zopv2HszRdsJ3_Etu94OWyT8nwa5zgkU8E44shAp27t88ptB2Jx_ZQN_EAjL_fcf6TDev7J6PpVlnI6MmZ7xh7_-Lyl4FXi80XBBqaQDo4d55Zi1xfohtsPs1iokDQNXQWyqjRoIJdcMvWLYXn=w1423-h943-no?authuser=0"
            )
        )
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
