from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import constants

app = Flask(__name__)

client = Client(constants.account_sid, constants.auth_token)

@app.route("/sms", methods=['POST'])
def sms_reply():
    reqData = request.json
    print(reqData)
    user_message = reqData['text']
    matches1 = ['hi', 'hello', 'hey']
    matches2 = ['chocolate', 'fry']
    matches3 = ['store', 'medium']
    matches4 = ['yes', 'yup', 'yeah']

    if any([x in user_message.lower() for x in matches1]):
        bot_response = constants.bot_response1
        print('Matched 1')
    elif all([x in user_message.lower() for x in matches2]):
        bot_response = constants.bot_response2
        print('Matched 2')
    elif any([x in user_message.lower() for x in matches3]):
        bot_response = constants.bot_response3
        print('Matched 3')
    elif any([x in user_message.lower() for x in matches4]):
        bot_response = constants.bot_response4
        print('Matched 4')
    else:
        bot_response = constants.bot_response_no_match
        print('Matched none')
    reqData['bot_response'] = bot_response

    client.messages.create(
        from_ = constants.from_sms_number,
        body = bot_response,
        to = constants.to_number
    )
    return reqData

    # Start TwiML response
    # resp = MessagingResponse()

    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")
    # return str(resp)

if __name__ == "__main__":
    app.run(debug=True)