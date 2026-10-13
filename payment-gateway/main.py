import requests

MERCHANT_ID = 'test'
CALLBACK_URL = 'http://localhost/callback'

def initiate_payment(amount, invoice_id=None):
    url = "https://api.novinopay.com/payment/ipg/v2/request"
    payload = {
        "merchant_id": MERCHANT_ID,
        "amount": amount,
        "callback_url": CALLBACK_URL,
        "invoice_id": invoice_id
    }
    headers = {
        "content-type": "application/json"
    }
    response = requests.post(url,json=payload,headers=headers)
    return response.json()
    
def generate_payment_url(authority):
    return f"https://ipg.novinopay.com/StartPay/Sandbox/{authority}"
    

def verify_payment(amount, authority):
    url = "https://api.novinopay.com/payment/ipg/v2/verification"
    payload = {
        "merchant_id": MERCHANT_ID,
        "amount": amount,
        "authority":authority,
    }
    headers = {
            "content-type": "application/json"
        }
    response = requests.post(url,json=payload,headers=headers)
    return response.json()


if __name__ == "__main__":
    
    amount_user = 200000
    result = initiate_payment(amount_user)
    authority = (result["data"]["authority"])
    
    payment_url = generate_payment_url(authority)
    print(payment_url)

    input("Interrupt for Verify...")
    
    verify_result = verify_payment(amount_user,authority)
    print(verify_result)