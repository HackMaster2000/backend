import base64
import requests

PAYPAL_CLIENT_ID = 'AbsNKHJpg8OE5NP3ME3BAd0poyT2bqO-PJlgWEFw7BzUN8sWOKjQlI6-4MYAgqOpkdS_lp283sE7KAfM'
PAYPAL_CLIENT_SECRET = 'EG--mOpvrWiFKv6yGJ1_rgmb7WotC9vVSK60hM27Zkphu7UfdtNC9EgFzEGw9KNFrRMrPd-FquzXmWon'
BASE_URL = "https://api-m.sandbox.paypal.com"

def generateAccessToken():
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise ValueError('no se hay credenciales')
    
    auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
    auth = base64.b64encode(auth.encode()).decode('utf-8')
    
    respose = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        data={"grant_type": "client_credentials"},
        headers={"Authorization": f"Basic {auth}"}
    )
    data = respose.json()
    return data['access_token']


def create_order(productos, amount):
    print(productos)
    
    try:
        access_token = generateAccessToken()
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": amount
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        
        response = requests.post(url, headers=headers, json=payload)
        print('--- response ---', response.json())
        return response.json()
    except Exception as error:
        print('*****')
        print(error)

def capture_order(orderID):
    access_token = generateAccessToken()
    url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{orderID}/capture"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.post(url, headers=headers)
    
    return response.json()