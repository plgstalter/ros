import time
import StravaPythonClient.swagger_client
import StravaPythonClient.swagger_client.rest as sr
from pprint import pprint
from sys import argv

# Configure OAuth2 access token for authorization: strava_oauth
if len(argv) == 2:
    StravaPythonClient.swagger_client.swagger_client.configuration.access_token = str(argv[1])
else:
    raise AttributeError('Rentrer la clef API svp')

# create an instance of the API class
api_instance = StravaPythonClient.swagger_client.swagger_client.AthletesApi()

try: 
    # Get Authenticated Athlete
    api_response = api_instance.getLoggedInAthlete()
    pprint(api_response)
except sr.ApiException as e:
    print("Exception when calling AthletesApi->getLoggedInAthlete: %s\n" % e)