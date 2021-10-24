#from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from sys import argv

# Configure OAuth2 access token for authorization: strava_oauth
if len(argv) == 2:
    swagger_client.configuration.access_token = str(argv[1])
else:
    raise AttributeError('Rentrer la clé API svp')

# create an instance of the API class
api_instance = swagger_client.AthletesApi()

try: 
    # Get Authenticated Athlete
    api_response = api_instance.getLoggedInAthlete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->getLoggedInAthlete: %s\n" % e)