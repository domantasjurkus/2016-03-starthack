import WebSmsComToolkit
import unirest
import json



ngrok = "http://ddebb152.ngrok.io"
aws = "http://54.93.76.242:5000"
swisscom = "+41794454421"

# Stuff needed to send back an SMS
username = 'domantas.jurkus@gmail.com'
password = 'Asdfghjk0'
gateway_url = 'https://api.websms.com'
message_text_unicode = "lalalal"
max_sms_per_message = 1
is_test = True


def receiveSMS(request):
    print "Handling"

    try:
        data = request.get_json()
        print
        print data['recipientAddress']
        print data['textMessageContent']
        print type(data)
    except Exception, e:
        return

    return_message = data['textMessageContent']


    response = unirest.post(
        "https://api.websms.com/rest/smsmessaging/text",
        headers = {
            "Authorization": "Bearer 1afe0f0a-de6a-4f9f-b77e-ccc7b79c494a",
            "Host": "api.websms.com",
            "Content-Type": "application/json"
        }, params = json.dumps({
            "messageContent" : "lffl",
            "recipientAddressList" : [ 41794454421 ]
        })
    )

    print return_message


    '''print response.code # The HTTP status code
    print response.headers # The HTTP headers
    print response.body # The parsed response
    print response.raw_body # The unparsed response'''


def getTemplateStubs():

    return {
        "taken" : [
            {
                "return_code": "lalala",
                "desc": "Nike Zoom V5 11.5"
            }, {
                "return_code": "zlhekt",
                "desc": "Zara Morning Blue Dress 46.3"
            }, {
                "return_code": "pqworw",
                "desc": "Logitech G933 Headset"
            }
        ],

        "purchased": [
            {
                "return_code": None,
                "desc": "Bobson Hamster Cage"
            }
        ],
        "returned": [
            {
                "return_code": "pqeror",
                "desc": "Swiss Cheese Family Pack"
            }, {
                "return_code": "mvdjwz",
                "desc": "Devious Lion Whip"
            }
        ]
    }