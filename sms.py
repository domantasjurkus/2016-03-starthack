import WebSmsComToolkit
import requests
import json
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


def receiveSMS(request, return_history):
    print "Handling"
    print return_history

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

        #if array[0] != "return":
        #    print "First keyword must be 'return' - exiting"
        #    return

        # Check if an order with such a code exists
        order_id = 00000001
        print "Making request to API"

        headers = {
            "X-Auth-Key": "68b675b75693809cf584712f3e9786fac04abb844365f2233ec94b182e4d091a",
            "Content-Type": "application/json"
        }
        print "betwqeen"
        response = requests.post(
            "https://testhorizon.gothiagroup.com/eCommerceServicesWebApi_ver339/api/v3/orders/"+str(order_id),
            headers=headers,
            data = {'key':'value'}
        )
        print response.code

        print "response code?"
        if response.code != 200:
            return

        print "response code == 200"

        print "got here"
        return_array = [
            array[1],
            "Description here",
            unicodedata.normalize('NFKD', data['recipientAddress']).encode('ascii','ignore'),
            "Win/fail",
            "Location"
        ]
        print "got here"
        print return_history
        return_history.append(return_array)
        print "return history:"
        print return_history

    except Exception, e:
        return

    return_message = data['textMessageContent']


    '''response = unirest.post(
        "https://api.websms.com/rest/smsmessaging/text",
        headers = {
            "Authorization": "Bearer 1afe0f0a-de6a-4f9f-b77e-ccc7b79c494a",
            "Host": "api.websms.com",
            "Content-Type": "application/json"
        }, params = json.dumps({
            "messageContent" : "lffl",
            "recipientAddressList" : [ 41794454421 ]
        })
    )'''

    # print return_message


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