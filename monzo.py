#!/usr/bin/env python
import requests


def get_balance(acc_id, token):
    '''
      Get user's balance
      returns float of current balance on user account
    '''
    params = {'account_id': acc_id}
    url = 'https://api.monzo.com/balance'
    response = requests.get(url=url,
                            headers={'Authorization': 'Bearer ' + token},
                            params=params)
    balance = float(response.json()['balance'] / 100)

    return balance


def get_transactions(acc_id, token, category=None):
    '''
      Get transactions
      returns list of a users transactions
    '''
    params = {'account_id': acc_id}
    url = 'https://api.monzo.com/transactions'
    response = requests.get(url=url,
                            headers={'Authorization': 'Bearer ' + token},
                            params=params)
    transactions = response.json()['transactions']

    if category is not None:
        filter_transactions = []
        for t in transactions:
            if t['category'] == category:
                filter_transactions.append(t)
        return filter_transactions

    return transactions
