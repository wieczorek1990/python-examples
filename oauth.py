from requests_oauthlib import OAuth2Session
from flask import Flask, redirect, request


OAUTH_URL = 'https://accounts.google.com/o/oauth2/%s'
CLIENT_ID = '897690190317-kjubs1pmrqlm9uhl45eb4ks8bt216f01.apps.googleusercontent.com'
CLIENT_SECRET = 'iK7i3JivIR7BeLnrpPfNF6FK'

refresh_token = ''

oauth = OAuth2Session(client_id=CLIENT_ID, redirect_uri='http://6f51c984.ngrok.io/oauth2callback', scope=['https://mail.google.com/'])
app = Flask(__name__)
app.debug = True


@app.route("/token")
def token():
    print oauth.authorization_url(OAUTH_URL % 'auth', access_type='offline', approval_prompt='force')[0]
    return ''


@app.route("/oauth2callback")
def oauth2callback():
    code = request.args.get('code')
    response = oauth.fetch_token(OAUTH_URL % 'token', client_secret=CLIENT_SECRET, client_id=CLIENT_ID, code=code)
    print response
    return ''


@app.route("/refresh")
def refresh():
    response = oauth.refresh_token(OAUTH_URL % 'token', refresh_token=refresh_token, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    print response
    return ''

if __name__ == "__main__":
    app.run()
