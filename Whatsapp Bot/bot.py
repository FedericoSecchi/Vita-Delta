import os
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

# Load Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Twilio WhatsApp number

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-message', methods=['POST'])
def send_message():
    user_number = request.json['number']  # User's number
    message_body = request.json['message']  # Message to send

    message = client.messages.create(
        body=message_body,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=f'whatsapp:{user_number}'
    )

    return {'status': 'Message sent', 'sid': message.sid}

if __name__ == '__main__':
    app.run(port=5000)
