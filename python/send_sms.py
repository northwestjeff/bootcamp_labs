from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3e1b0ddf6b06eaef853287400f6442d4"
# Your Auth Token from twilio.com/console
auth_token  = "9cecf0a8ee5e6fcb77b46ceec7aa5d70"

client = Client(account_sid, auth_token)

send_number = input("who would you like to send a text to?: ")
send_number = str(("{}{}".format("+1", send_number)))
print("")
message_to_send = input("What would you like to send as a text message?: ")

message = client.messages.create(
    to=send_number,
    from_="+15414352840",
    body=message_to_send)

print(message.sid)
