import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
ALERT_PHONE = os.getenv("ALERT_PHONE")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms_alert(risk, confidence):

    message_body = f"""
    ⚠ FLOOD ALERT
    Risk: {risk}
    Confidence: {confidence:.2f}%
    """

    try:
        client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=ALERT_PHONE
        )
        print("SMS Alert Sent")

    except Exception as e:
        print("SMS failed:", e)