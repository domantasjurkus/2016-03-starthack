import WebSmsComToolkit

ngrok = "http://ddebb152.ngrok.io"
aws = "http://54.93.76.242:5000/receive_sms"
swisscom = "+41794454421"

# Stuff needed to send back an SMS
username = 'domantas.jurkus@gmail.com'
password = 'Asdfghjk0'
gateway_url = 'https://api.websms.com'
recipient_address_list = [4367612345678L]
message_text_unicode = "Hello there"
max_sms_per_message = 1
is_test = True


def receiveSMS(request):
    print "Handling"

    data = request.get_json()
    print data['recipientAddress']
    print data['textMessageContent']
    print type(data)

    # Check if the message follows a ['return', return_code, manager_id] format
    client = WebSmsComToolkit.Client(gateway_url, username, password)
    client.verbose = True
    response = client.send("message", max_sms_per_message, is_test)

    print "-- Response Object --"
    print "transferId : " + str(response.transferId)
    print "clientMessageId : " + str(response.clientMessageId)
    print "statusCode : " + str(response.statusCode)
    print "statusMessage : " + str(response.statusMessage)
    print "rawContent : " + str(response.rawContent)

def getTemplateStubs():

    return {
        "taken": [
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