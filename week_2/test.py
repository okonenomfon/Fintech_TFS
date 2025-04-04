import requests

url = "https://api.paystack.co/transaction/initialize"

headers = {
    "Authorization" : "Bearer sk_test_----eno----",                                                                                                  #f3cd9e4396d2f0f7616374ce97583acc4cdba25f
    "Content-Type" : "application/json"
}

data = {
    "email" : "enomfon20@gmail.com",
    "amount" : 50000,
    "callback_url" : "http://localhost:5000/callback"
}

response = requests.post(url, headers=headers, json=data)

print(response.json())