#!/usr/bin/env python
import requests

def get_balance(acc_id, token):
	'''
	  Get user's balance
	  returns float of current balance on user account
	'''
	params = {'account_id': acc_id}
	url = 'https://api.monzo.com/balance'
	response = requests.get(url=url, headers={'Authorization': 'Bearer ' + token}, params=params)
	balance = float(response.json()['balance'] / 100)

	return balance