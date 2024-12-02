def getUniqueEvents(event_api, team_given):
    eventList = event_api.get_team_events_by_year(team_given, 2023)
    eventKeyList = []
    
    for i in eventList:
        eventKeyList.append(i.key)

    return eventKeyList

def getUniqueTeams(team_api, eventList):
    names_numbers = []
    countries = []
    states = []
    cities = []

    for event in eventList:
        teams = team_api.get_event_teams(event)

        for t in teams:
            if not ([t.nickname, t.team_number] in names_numbers):
                names_numbers.append([t.nickname, t.team_number])
            if not (t.country in countries):
                countries.append(t.country)
            if not (t.state_prov in states):
                states.append(t.state_prov)
            if not (t.city in cities):
                cities.append(t.city)
        
        return [names_numbers, countries, states, cities ]

