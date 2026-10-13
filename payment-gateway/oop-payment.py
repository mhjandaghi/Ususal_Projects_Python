from abc import ABC,abstractmethod
import requests
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class InitiatePaymentResponse():
    success : bool
    message : str
    code : str
    authority : Optional[str] = None
    raw : dict = field(default_factory=dict)
    
@dataclass
class VerifyPaymentResponse():
    success : bool
    message : str
    code : str
    ref_id : str
    trans_id : Optional[str] = None
    raw : dict = field(default_factory=dict)

class NetworkError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)
        
class AbstractPaymentGateway(ABC):
    request_timeout = 30
    
    @abstractmethod
    def initiate_payment(self, amount, invoice_id=None):
        pass
    @abstractmethod
    def generate_payment_url(self, authority):
        pass
    @abstractmethod
    def verify_payment(self, amount, authority):
        pass
    @abstractmethod
    def activate_sandbox(self):
        pass
    
    def _make_request(self, url, payload):
        headers = {
            "content-type": "application/json"
        }
        try:
            
            response = requests.post(url,json=payload,headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.Timeout:
            raise NetworkError("connection Error", error_code=408)
        except requests.HTTPError:
            raise NetworkError("http error", error_code= response.status_code)
        except requests.ConnectionError:
            raise NetworkError("Http Connection Error", error_code=503)
        except requests.RequestException:
            raise NetworkError("request exception", error_code=500)

    
class NovinoPayGateway(AbstractPaymentGateway):
    payment_init_url = "https://api.novinopay.com/payment/ipg/v2/request"
    payment_verify_url = "https://api.novinopay.com/payment/ipg/v2/verification"
    payment_gateway_url = "https://ipg.novinopay.com/StartPay/"
    success_status_codes = [100, 101]

    def __init__(self, merchant_id, callback_url, sandbox=True):
        self.merchant_id = merchant_id
        self.callback_url = callback_url
        if sandbox:
            self.activate_sandbox()
            
    def initiate_payment(self, amount, invoice_id=None, **kwargs):
        payload = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "callback_url": self.callback_url,
            "invoice_id": invoice_id
        }
        
        if name := kwargs.get("name"):
            payload.update({'name': name})
            
        # return response.json()
        response = self._make_request(self.payment_init_url,payload)
        if int(response['status']) in self.success_status_codes:
            return InitiatePaymentResponse(
                success=True,
                message=response["message"],
                code= response["status"],
                authority= response["data"]["authority"]
            )
        else:
            return InitiatePaymentResponse(
                success=False,
                message=response["message"],
                code= response["status"],
                authority= None
            )
    def generate_payment_url(self,authority):
        return self.payment_gateway_url + str(authority)

    def verify_payment(self, amount, authority):
        payload = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "authority":authority,
        }
        response = self._make_request(self.payment_verify_url,payload)
       
        if int(response['status']) in self.success_status_codes:
            return VerifyPaymentResponse(
                success=True,
                message=response["message"],
                code= response["status"],
                ref_id= response["data"]["ref_id"],
                trans_id= response["data"]["trans_id"]
            )
        else:
            return VerifyPaymentResponse(
                success=False,
                message=response["message"],
                code= response["status"],
                ref_id= response["data"]["ref_id"],
                trans_id= response["data"]["trans_id"]
            )
    
    
    def activate_sandbox(self):
        self.payment_init_url = "https://api.novinopay.com/payment/ipg/v2/request"
        self.payment_verify_url = "https://api.novinopay.com/payment/ipg/v2/verification"
        self.payment_gateway_url = "https://ipg.novinopay.com/StartPay/Sandbox/"
        self.merchant_id = "test"
        
if __name__ == "__main__":
    amount_user = 200000
    payment_client = NovinoPayGateway("test", "http://localhost/callback")
    result = payment_client.initiate_payment(amount_user)
    print(result)
    
    authority = result.authority
    
    payment_url = payment_client.generate_payment_url(authority)
    print(payment_url)

    input("Interrupt for Verify...")
    
    verify_result = payment_client.verify_payment(amount_user,authority)
    print(verify_result)