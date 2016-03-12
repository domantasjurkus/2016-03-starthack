import requests

BASE_URL = "https://testhorizon.gothiagroup.com/eCommerceServicesWebApi_ver339/"
API_KEY = "2d64db29fea4adbed35825365c334d75640eb92ae38020b640de66b93c952023"


def generate_billingCustomer():
    # address = {"Street": "Main",
               # "PostalCode": "12345",
               # "PostalPlace": "",
               # "CountryCode": "USA"}
    data = {"ConversationLanguage": "English",
            "FirstName": "Harrison",
            "LastName": "Pincket",
            #"Address": address,
            "order": 1}
    return {"billingCustomer": data}


def swagger_checkout():
    headers = {'X-Auth-Key': API_KEY}
    val = generate_billingCustomer()
    data = {"body":val}
    r = requests.post(BASE_URL + "/api/v3/checkout", headers=headers, data=data)
    return r.text

print(swagger_checkout())
