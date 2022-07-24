import requests
import json

tokenURI =  {
            "name": "SKU",
            "index": 0,
            "description": "Sku artwork",
            "medium": "image",
            "dimensions": { "width": "100", "height": "100" },
            "image": "https://www.example.com/image.jpg",
            "Provenance": "Galerie Claude Lemand, Paris, Acquired directly from the above by the current owner, 2015",
            "CertificateOfAuthenticity": "Available | by Galerie Claude Lemand",
            "Current location": "Dubai, United Arab Emirates",
            "external_url": "https://www.example.com/image.jpg"
        }
    
def test_mint():
    # Get the data from the request
    data = {
        "to": "0xEf35ea8a78BaBDA26AF66d03b26FBe0f4F5065aD",
        "tokenURI": tokenURI
    }
    # Send the request
    r = requests.post('http://localhost:5000/mint', json=data)
    return json.loads(r.text)

def test_balance():
    # Get the data from the request
    data = {
        "address": "0xEf35ea8a78BaBDA26AF66d03b26FBe0f4F5065aD"
    }
    # Send the request
    r = requests.post('http://localhost:5000/balance', json=data)
    return json.loads(r.text)


def test_uri():
    # Get the data from the request
    data = {
        "tokenID": 2
    }
    # Send the request
    r = requests.post('http://localhost:5000/uri', json=data)
    return json.loads(r.text)


def test_owner():
    # Get the data from the request
    data = {
        "tokenID": 2
    }
    # Send the request
    r = requests.post('http://localhost:5000/owner', json=data)
    return json.loads(r.text)

def test_tokens():
    # Get the data from the request
    data = {
        "address": "0xEf35ea8a78BaBDA26AF66d03b26FBe0f4F5065aD"
    }
    # Send the request
    r = requests.post('http://localhost:5000/tokens', json=data)
    return json.loads(r.text)

def test_transfer():
    # Get the data from the request
    data = {
        "from": "0xEf35ea8a78BaBDA26AF66d03b26FBe0f4F5065aD",
        "to": "0xF05fF29bb39C6e897456aAa5276fdDd8dEa97fc9",
        "tokenID": 2
    }
    # Send the request
    r = requests.post('http://localhost:5000/transfer', json=data)
    return json.loads(r.text)


""" uncomment the following lines to run the tests """
#print(test_mint())
#print(test_balance())
print(test_uri())
#print(test_owner())
#print(test_tokens())
#print(test_transfer())