
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from services.first_aid import search_injury
from utils.message import convert_result_to_message

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/whatsapp', methods=['POST'])
def reply_with_first_aid():
    ailment = request.values.get('Body')
    print('Message sent', ailment)
    treatments = search_injury(ailment)
    message = convert_result_to_message(treatments)
    response = MessagingResponse()
    response.message(message)
    return str(response)


if __name__ == '__main__':
    app.run()