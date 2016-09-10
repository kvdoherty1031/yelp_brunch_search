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

def make_params(location):
	businesslist = []
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
	for business_returned in results.businesses:
		if (business_returned.rating > 3):
			print(business_returned.name, business_returned.rating)
			if len(businesslist)<3:
				businesslist.append("{} -  RATED: {}   PHONE#: {}   ADDRESS: {}" .format(business_returned.name, 
					business_returned.rating, business_returned.phone, 
					business_returned.location.display_address))
				print(businesslist)
				if len(businesslist)==3:
					return(businesslist)
	






