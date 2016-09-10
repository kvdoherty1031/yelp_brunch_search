from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEYCODE'],
    consumer_secret=os.environ['CONSUMER_SECRETCODE'],
    token=os.environ['TOKENCODE'],
    token_secret=os.environ['TOKEN_SECRETCODE']
)


businesslist = []

def make_params(location):
	parameterone = "brunch"
	client = Client(auth)
	parameters_for_search = {
		"term": parameterone,
		"lang": 'en',
	}
	client.search(location, **parameters_for_search)
	results = client.search(location)
	results.businesses
	results.businesses[0].name
	# print(results.businesses[0])
	for business_returned in results.businesses:
		if (business_returned.rating > 3 and business_returned.rating <= 4):
			print(business_returned.name, business_returned.rating)
			# print(business_above_four)
			if len(businesslist)<3:
				businesslist.append("{} -  RATED: {}   PHONE#: {}   ADDRESS: {}" .format(business_returned.name, 
					business_returned.rating, business_returned.phone, 
					business_returned.location.display_address))
				print(businesslist)
				if len(businesslist)==3:
					return(businesslist)
	






