# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6YKHwMgHizjpu7yKbON7WKV4i_II4_g
"""

import json
import requests
from pprint import pprint 
import time


address = ['0xeca19b1a87442b0c25801b809bf567a6ca87b1da', '0xee889cdf628e138f15538304fd72e2af56cbe4b6', '0x4b41947e269464408bbd9dce7346a7e07d522b12', '0x38e26c68bdef7c6e7f1aea94b7ceb8d95b11bd69', '0x873ce5c27fe1a679b724e25b5a856282a93b137f','0x936146f6850dc157e77fc060c442e0bdffbbe6ff', '0x70462d3278dac620a4d2c7ae674bc46c6916974e', '0x873ce5c27fe1a679b724e25b5a856282a93b137f', '0x4b41947e269464408bbd9dce7346a7e07d522b12', '0x711447b288e2f853fa9716aa8eba37b02ca8a50f', '0x11759e580b444aa1136482929984c76a19ef2794', '0x04bb39f36bbadf4e31aa1df09a2f5a0b76114a62', '0x8d16abfba10c079340ddf2b252f94353cdccfa57', '0x8f8d0e8c921b6fbee6da796f3c823a8a1e354bea', '0xabde0e83ba513891aa3bc0a2f796132cae026106', '0x635893f9918cbb41cb6c6bde4a87e5959f53dd56']
address = set(address.copy())
address = sorted(address.copy())

send = dict()
recieve = dict()

for addr in address:
  send[addr] = 0
  recieve[addr] = 0

recieve['0xeca19b1a87442b0c25801b809bf567a6ca87b1da'] = 20 * (10**18)
recieve['0x873ce5c27fe1a679b724e25b5a856282a93b137f'] = 35 * (10*18)


for addr in address:
  if addr == '0x873ce5c27fe1a679b724e25b5a856282a93b137f':
    continue
  url = "https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address="+ addr.lower() +"&startblock=0&endblock=999999999&sort=asc&apikey=K7ST5DC6VP2Z5ZVWWD1IB3JDB5AHIEV274"
  headers = {'content-type': 'application/json', 'User-Agent': 'curl/7.47.1'}
  response = requests.get(url, headers = headers)
  data = response.json()
  transaction = data['result']

  n = len(transaction)

  for i in range(n):
    if transaction[i]['tokenSymbol'] == 'BKTC':
      send[addr] += int(transaction[i]['value'])
      recieve[transaction[i]['to']] += int(transaction[i]['value'])
      print('Tx hash: ', transaction[i]['hash'])
      print('From: ', addr)
      print('To: ', transaction[i]['to'])
      print('Amount Tranfer: ', transaction[i]['value'])
      print('-------------------------------------------')
  time.sleep(1)

for i in address:
  print('Address: ', i)
  print('Balance: ', recieve[i] - send[i])
  print('-----------------------------------')

