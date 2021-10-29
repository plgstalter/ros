import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from sys import argv

if len(argv) < 3:
    raise AttributeError('rentrer les bonnes donnes svp!')
    # bonnes donnees : python requetes.py type_requete access_token [infos supplémentaires]

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = str(argv[2])

if argv[1] == 'gear_id':
    # create an instance of the API class
    api_instance = swagger_client.api.gears_api.GearsApi()
    id = 'g7518998' # String | The identifier of the gear.

    try: 
        # Get Equipment
        api_response = api_instance.get_gear_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GearsApi->getGearById: %s\n" % e)
elif argv[1] == 'get_activities':

    # create an instance of the API class
    api_instance = swagger_client.api.activities_api.ActivitiesApi()
    before = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
    after = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
    page = 56 # Integer | Page number. Defaults to 1. (optional)
    perPage = 56 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

    try: 
        # List Athlete Activities
        api_response = api_instance.get_logged_in_athlete_activities(before=before, after=after, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)
