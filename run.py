from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    response = MessagingResponse()
    response.message('Thank you response. '
                     'We would reach out to you soon')
    return str(response)

if (__name__ == '__main__'):
    app.run(debug=True)

