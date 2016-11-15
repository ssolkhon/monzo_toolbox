# Monzo Toolbox
I created this so I had a way to easily collect receipts for my Monzo transactions when I was working away and needed to supply receipts for my expenses. If I find more uses for the Monzo API in the future, I will add more functionality to this app.

#### Current functionality:
- Show users balance
- Save receipts

#### Authentication:
The Monzo API implements OAuth 2.0 to allow users to log in to applications without exposing their credentials. I haven't properly implemented the authentication steps for this app to generate a token, but you can get a temporary access token by visiting the developer tools (https://developers.getmondo.co.uk/).

#### How to run:

Step 1) Clone the repo 

```
$ git clone <repo url>
```

Step 2) Create a virtual env

```
$ virtualenv --python=python3 monzo_toolbox
$ source monzo_toolbox/bin/activate
```

Step 3) Install dependencies
```
$ pip install -r requirements.txt
```

Step 4) Create credentials.py
```
$ cp credentials.py.sample credentials.py
$ nano credentials.py
```
Enter your key and user id.

Step 5) Run the app. Remember to first check that the correct function is enabled in main.py.
```
$ ./main.py
```