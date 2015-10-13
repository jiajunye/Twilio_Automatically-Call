import webapp2
from twilio import twiml
import urllib2
import json

# Parse json format of the front page of reddit to fetch the top headline
url = 'http://reddit.com/.json?limit=1'
request = urllib2.Request(url)
json = json.loads(urllib2.urlopen(request).read())
headline = json['data']['children'][0]['data']['title']

# Autocall handler used to response Twilio's HTTP request
class Autocall(webapp2.RequestHandler):
    def post(self):
    	# Response to incoming requests
    	r = twiml.Response()
        r.say("Good afternoon Dan, my name is Jason")
        r.say("The top headline on the front page of Reddit is " + headline)
        # Add a short pause
        r.pause()
        r.say("Have a nice day. Goodbye")
        # Set header content type to text/xml
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(str(r))

app = webapp2.WSGIApplication([('/twiml', Autocall)],
                              debug=True)