from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC18c49e9808e29af42c4f37ccd1dd70c5'
auth_token = 'd9c648f24d1100f19abf58bb3677e1e5'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Is the second sattai movie over???.",
                     from_='+13346036945',
                     to='+919884033582'
                 )

print(message.sid)