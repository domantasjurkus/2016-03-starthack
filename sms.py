import requests
import unicodedata



ngrok = "http://0c8a9301.ngrok.io"
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
        print data['recipientAddress']
        print data['textMessageContent']

        if data['textMessageContent'] == "":
            print "Text message content empty - exiting..."
            return


        string = data['textMessageContent'].lower()
        string = unicodedata.normalize('NFKD', string).encode('ascii','ignore')
        array = string.split()

        # Try and return the order using the internal API
        print "Making request to API"

        headers = {
            #"X-Auth-Key": "68b675b75693809cf584712f3e9786fac04abb844365f2233ec94b182e4d091a",
            #"Content-Type": "application/json"
        }
        print "between"
        r = requests.post('http://localhost:5000/return/sms/',
            headers=headers,
            data={'orderNumber': str(array[1]), 'managerCode': str(array[2])}
        )

        print r

    except Exception, e:
        return


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
