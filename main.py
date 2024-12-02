from __future__ import print_function

import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint

import utilfuncs as uf

# Defining the host is optional and defaults to https://www.thebluealliance.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = tbaapiv3client.Configuration(
    host = "https://www.thebluealliance.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration = tbaapiv3client.Configuration(
    host = "https://www.thebluealliance.com/api/v3",
    api_key = {
        'X-TBA-Auth-Key': 'GydDDUgyvaGJytFlVZEJxnKdg1Ut19H1PfRwrAzFwakpYtdfcLYf4omQLvFPaTf3'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'


# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    event_api = tbaapiv3client.EventApi(api_client)
    team_api = tbaapiv3client.TeamApi(api_client)

    try:
        team_number = input("Enter the FRC team you would like to learn about: ")
        events = uf.getUniqueEvents(event_api, f"frc{team_number}")
        team_info = uf.getUniqueTeams(team_api, events)

        print(f"Teams team {team_number} faced: ")
        for team in team_info[0]:
            print(f"Team {team[1]}: {team[0]}")

        print()

        print(f"Countries that have faced this team: ")
        for country in team_info[1]:
            print(country)
        
        print()

        print(f"States that have faced this team: ")
        for state in team_info[2]:
            print(state)
        
        print(f"Cities that have faced this team: ")
        for city in team_info[3]:
            print(city)
 
    except ApiException as e:
        print("Exception when calling TBAApi->get_status: %s\n" % e)