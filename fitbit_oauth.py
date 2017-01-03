from requests_oauthlib import OAuth2Session
from flask import Flask, redirect, request


SERVER_ROOT = 'http://be30eb66.ngrok.io/'
OAUTH_ROOT = 'https://www.fitbit.com/oauth2/'
CLIENT_ID = '227VLX'
CLIENT_SECRET = 'b4bb0d2b6fcb1a3b80d2a182d25bc392'
SCOPE = ['activity', 'nutrition', 'heartrate', 'location', 'nutrition', 'profile', 'settings', 'sleep', 'social', 'weight']

app = Flask(__name__)
app.debug = True
oauth = OAuth2Session(client_id=CLIENT_ID, redirect_uri=SERVER_ROOT + 'integrations/fitbit/callback', scope=SCOPE, response_type='code')
refresh_token = ''


@app.route("/")
def authorize():
    response = oauth.authorization_url(OAUTH_ROOT + 'authorize', expires_in=60)
    print response
    return ''


@app.route("/integrations/fitbit/callback")
def callback():
    print request
    code = request.args.get('code')
    response = oauth.fetch_token(OAUTH_ROOT + 'token', client_secret=CLIENT_SECRET, client_id=CLIENT_ID, code=code)
    print response
    return ''


@app.route("/integrations/fitbit/tokens/refresh")
def refresh():
    response = oauth.refresh_token(OAUTH_ROOT + 'token', refresh_token=refresh_token, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    print response
    return ''

if __name__ == "__main__":
    app.run()

