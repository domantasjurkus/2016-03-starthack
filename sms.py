ngrok = "http://4b1b5183.ngrok.io"
swisscom = "+41794454421"

'''
username = 'domantas.jurkus@gmail.com'
password = 'Asdfghjk0'
gateway_url = 'https://api.websms.com'
recipient_address_list = [4367612345678L]
message_text_unicode = "Hello there"
max_sms_per_message = 1
is_test = True
'''

def receiveSMS(request):
    print "Handling"

    data = request.get_json()
    print data['recipientAddress']
    print data['textMessageContent']
    print type(data)