#!/usr/bin/env python
import credentials
import monzo

def main():
	my_balance = monzo.get_balance(credentials.my_acc_id, credentials.my_token)
	print('Your balance is: £' + str(my_balance))


if __name__ == '__main__':
    # Run app
    main()