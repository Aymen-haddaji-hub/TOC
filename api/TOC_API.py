#!/usr/bin/python3
"""
TOC_API.py
Description: This file contains the TOC_API
a Flask API that uses the Ehtereum blockchain to Mint NFTs
Author: Aymen Haddaji
"""

import json
from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Initialize the Web3 connection - load the abi and contract address
w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/f340c5e657604f199ea6f7a2301c1bc3'))
abi = json.loads(open('../build/contracts/TheOpenCrate.json').read())
contract_address = '0x06Fa8EA30B6393ec15ff083FD15a51610cea84B9'
toc = w3.eth.contract(abi=abi['abi'], address=contract_address)
master_address = '0xEf35ea8a78BaBDA26AF66d03b26FBe0f4F5065aD'


# API endpoint to mint a new NFT
@app.route('/mint', methods=['POST'])
def mint():
    data = request.get_json()
    to = data['to']
    tokenURI = str(data['tokenURI'])
    print((type(tokenURI)))
    # Mint the NFT
    tx = toc.functions.mintNFT(to, tokenURI).buildTransaction({
        'from': master_address,
        'nonce': w3.eth.getTransactionCount(master_address),
        'chainId': 3,
        'gas': 1000000,
        'gasPrice': w3.eth.gasPrice
    })
    signed_tx = w3.eth.account.signTransaction(tx, "96d25a533705a76e3ff76573f393a1d61a91735fb8cc21f3df87ee8846716a44")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(w3.toHex(tx_hash))
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return jsonify({'tx_hash': w3.toHex(tx_hash)})


# API endpoint to get the balance of an address
@app.route('/balance', methods=['POST'])
def balance():
    data = request.get_json()
    address = data['address']
    balance = toc.functions.balanceOf(address).call()
    return jsonify({'Current NFTs balance': balance})


# API endpoint to get the URI of an NFT
@app.route('/uri', methods=['POST'])
def uri():
    data = request.get_json()
    tokenID = data['tokenID']
    #w3.toInt(tokenID)
    uri = toc.functions.tokenURI(tokenID).call()
    return jsonify({'tokenURI': uri})


# API endpoint to get the owner of an NFT
@app.route('/owner', methods=['POST'])
def owner():
    data = request.get_json()
    tokenID = data['tokenID']
    owner = toc.functions.ownerOf(tokenID).call()
    return jsonify({'owner': owner})


# API endpoint to get all the NFTs owned by an address
@app.route('/tokens', methods=['POST'])
def tokens():
    data = request.get_json()
    address = data['address']
    tokens_list = []
    tokens = toc.functions.balanceOf(address).call()
    print(tokens)
    for token in range(tokens):
        int(token)
        uri = toc.functions.tokenURI(1).call()
        dic = {'tokenID': token, 'tokenURI': uri}
        tokens_list.append(dic)
    return jsonify({'tokens': tokens_list})

# API endpoint to transfer an NFT
@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    tokenID = data['tokenID']
    sender = data['from']
    to = data['to']
    # Transfer the NFT
    tx = toc.functions.transferFrom(sender, to, tokenID).buildTransaction({
        'from': master_address,
        'nonce': w3.eth.getTransactionCount(master_address),
        'chainId': 3,
        'gas': 1000000,
        'gasPrice': w3.eth.gasPrice
    })
    signed_tx = w3.eth.account.signTransaction(tx, "96d25a533705a76e3ff76573f393a1d61a91735fb8cc21f3df87ee8846716a44")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(w3.toHex(tx_hash))
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return jsonify({'tx_hash': w3.toHex(tx_hash)})


# run the application
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

