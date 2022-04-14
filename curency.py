import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/19abb2dd64cc30bc634b944a/pair/USD/ILS'


# Making our request
response = requests.get(url)
data = response.json()
#length = (len(data['conversion_rate']))
print (data["conversion_rate"])


