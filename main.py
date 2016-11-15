#!/usr/bin/env python
import os

import credentials
import monzo
import images


def print_balance():
    my_balance = monzo.get_balance(credentials.my_acc_id, credentials.my_token)
    print('Your balance is: £' + str(my_balance))


def save_receipts():
    my_path = 'reciepts'
    my_trancactions = monzo.get_transactions(
        credentials.my_acc_id,
        credentials.my_token, 'expenses')

    if len(my_trancactions) > 0:
        # Create directory for reciepts
        if not os.path.isdir(my_path):
            print('Creating reciept directory...')
            os.makedirs(my_path)

    # Save reciept files
    for t in my_trancactions:
        print('Saving imgae: ' + t['id'] + '.jpg')
        if len(t['attachments']) > 0:
            result = t['attachments'][0]['url']
            images.save_image_from_url(result, my_path + '/' + t['id'])

if __name__ == '__main__':
    # Run app
    save_receipts()
