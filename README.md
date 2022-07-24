# The Open Crate Blockchain

## What is the Open Crate Blockchain?
the following is a description of the Open Crate Blockchain

the project is a set of smart contracts that are designed to allow on a top of decentralized blockchain 
to manipulate and leverage the 

## Starting the project
```
git clone repository_url
```
for an easy way to execute and deploy the api you should use the following command
```
cd TOC
docker build -t project_name .
docker run -p 5000:5000 -d project_name
```
now the api is running on port 5000 you can start send requests to the api
existing the project you can stop the api with the following command
```
docker stop project_name
```


## Structure of the Open Crate Blockchain

Part 1:
#### The Open Crate smart contract

the following directory contains the Open Crate smart contract and the artifacts that are required to deploy it

```
contracts/
build/
migrations/
tests/
```

the contracts are tested and deployed to the ROPSTEN network
the Production network is not yet deployed

Part 2:
##### The Open Crate Blockchain API

the directory contains the Open Crate Blockchain API

``` 
api/
```

a flask application is used to serve the API
 ## API Endpoints

route ```/api/mint``` 
#### description
 a method that allows a user to mint a new NFT
 an address and tokenURI ( aka token info) are required
#### example of request body

 ```
 {
  "to": "0x0000000000000000000000000000000000000000",
  "tokenURI": tokenURI
 }
 ```
 ### the Following schema Of tokenURI is required by project owner:
 
 ``` 
tokenURI =  
{
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
 ```
the endpoint returns a transaction hash
#### example:
```
{'tx_hash': '0x78b43a575c9c790fa3130bbc5eabb3f871fdc45afe1f20fb908e6383f230c12f'}
```

## Balance endpoint

route ``` /api/balance ```
#### description: returns the balance of the user
#### example of request body:
```
{
  "address": "0x0000000000000000000000000000000000000000"
}
```
#### example of response body:
```
{
  "Current NFTs balance": "0"
}
```

## uri endpoint
route ``` /api/uri ```
#### description: returns the uri of the token
#### example of request body:
```
{
  "tokenId": 1
}
```
#### example of response body:
```
{'tokenURI': '{"attributes": [{"name": "SKU", "index": 0, "description": "Sku artwork", "medium": "image", "dimensions": {"width": "100", "height": "100"}, "image": "https://www.example.com/image.jpg", "Provenance": "Galerie Claude Lemand, Paris, Acquired directly from the above by the current owner, 2015", "CertificateOfAuthenticity": "Available | by Galerie Claude Lemand", "Current location": "Dubai, United Arab Emirates", "external_url": "https://www.example.com/image.jpg"}]}'}
```

## owner endpoint
route ``` /api/owner ```
#### description: returns the owner of the token
#### example of request body:
```
{
  "tokenId": 1
}
```
#### example of response body:
```
{'owner': '0x0000000000000000000000000000000000000000'}
```


## transfer endpoint
route ``` /api/transfer ```
#### description: transfers the token to a new owner
#### example of request body:
```
{
    "from": "0x0000000000000000000000000000000000000000",
    "to": "0x0000000000000000000000000000000000000000",
    "tokenId": 1
}
```
#### example of response body:
```
{'tx_hash': '0x78b43a575c9c790fa3130bbc5eabb3f871fdc45afe1f20fb908e6383f230c12f'}
```

## tokens endpoint
route ``` /api/tokens ```
#### description: returns all the tokens of the user and their uri
#### example of request body:
```
{
  "address": "0x0000000000000000000000000000000000000000"
}
```
#### example of response body
```
{
  "tokens": [
    {
      "tokenId": 1,
      "tokenURI": "{"attributes": [{"name": "SKU", "index": 0, "description": "Sku artwork", "medium": "image", "dimensions": {"width": "100", "height": "100"}, "image": "https://www.example.com/image.jpg", "Provenance": "Galerie Claude Lemand, Paris, Acquired directly from the above by the current owner, 2015", "CertificateOfAuthenticity": "Available | by Galerie Claude Lemand", "Current location": "Dubai, United Arab Emirates", "external_url": "https://www.example.com/image.jpg"}]}"
    }
  ]
}
```

