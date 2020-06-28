from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'put account sid here'
auth_token = 'put auth token here'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test!",
                     from_='put twilio phone number here',
                     to='put recipient phone number here'
                 )

print(message.sid)