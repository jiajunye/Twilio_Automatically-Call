I used Python and Google App Engine Platform for this Twilio auto call application.

Firstly, I created a new application and added Twilio's Python library to this app.

Secondly, I created autocall.py to build the handler which will be used to response Twilio's HTTP request. Added read content to post method including my name and the top headline on the front page of reddit which I fetched by parsing json format of the front page of reddit.

Then, deployed the app to GAE. After that, I was able to send a POST request to http://helloworld-twilio.appspot.com/twiml.

Next, I copied and pasted the http://helloworld-twilio.appspot.com/twiml URL into the "Voice" URL box on my Twilio Account.

Finally, I created make_call.py to make the auto call by using Twilio's REST API. Scheduled the call time to 7:00pm UTC, October 12th, 2015.