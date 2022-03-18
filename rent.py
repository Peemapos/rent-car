import json
from web3 import Web3
import RPi.GPIO as GPIO
from time import sleep

web_3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainid=1377
address=input("Input your address: ")
private_key=input("Input your privatekey:0x")
host="0xd95eF0F66BA6adAf5c23F467B2fEdc3247d5a77c"

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
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while (True):    
            
            
        GPIO.output(18, 1)
            

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
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while (True):    
            
            
        GPIO.output(18, 1)
            
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
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while (True):    
            
            
        GPIO.output(18, 1)
            
