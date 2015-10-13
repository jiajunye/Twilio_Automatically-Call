# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import time
from datetime import datetime, date, time

# Get these credentials from http://twilio.com/user/account
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

# Set the automatically call time at 7:00pm UTC, October 12th, 2015
d = date(2015, 10, 12)
t = time(19, 0)
scheduled_calltime = datetime.combine(d, t)

while True:
	# Show the countdown on terminal.
	print datetime.utcnow()
	# Automatically make the call on 7:00pm UTC, October 12th, 2015.
	if datetime.utcnow().hour == scheduled_calltime.hour and datetime.utcnow().minute == scheduled_calltime.minute:
		call = client.calls.create(to="+1xxxxxxxxxx", 
								   from_="+1yyyyyyyyyy", 
								   url="http://helloworld-twilio.appspot.com/twiml")
		# Once the call made, terminate the loop.
		break
# Print this Call SID on terminal
print call.sid