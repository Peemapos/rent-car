from web3 import Web3
import json
from time import sleep
#import RPi.GPIO as GPIO

web_3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainid=1377
address=input("Input your address: ")
private_key=input("Input your privatekey:0x")
host="0x97C7A1FEe860a8686cDd0A7F179F17AE36Df92cC"

nonce=web_3.eth.getTransactionCount(address)
day=input("How many day: ")
if day == "1":
    pay = {
        'nonce': nonce,
        'to': host,
        'value': web_3.toWei(1, 'ether'),
        'gas': 2000000,
        'gasPrice': web_3.toWei('50', 'gwei')
    }

    #sign the transaction
    signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

    #send transaction
    pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
    print("You rent 1 day")

if day == "3":
    pay = {
        'nonce': nonce,
        'to': host,
        'value': web_3.toWei(3, 'ether'),
        'gas': 2000000,
        'gasPrice': web_3.toWei('50', 'gwei')
    }

    #sign the transaction
    signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

    #send transaction
    pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
    print("You rent 3 day")
if day == "7":
    pay = {
        'nonce': nonce,
        'to': host,
        'value': web_3.toWei(7, 'ether'),
        'gas': 2000000,
        'gasPrice': web_3.toWei('50', 'gwei')
    }

    #sign the transaction
    signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

    #send transaction
    pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
    print("You rent 7 day")
