from stravalib.client import Client

client = Client()
authorize_url = client.authorization_url(client_id=3516, redirect_uri='http://localhost:5000/authorized')
# Have the user click the authorization URL, a 'code' param will be added to the redirect_uri
# .....

# Extract the code from your webapp response
code = request.get('code') # or whatever your framework does
access_token = client.exchange_code_for_token(client_id=3516, client_secret='asdf1234', code=code)

# Now store that access token somewhere (a database?)
client.access_token = access_token
athlete = client.get_athlete()
print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))