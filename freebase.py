import json
import urllib.request
import urllib.parse
api_key = open(".freebase_api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
def get_types(name):
    query = [{'name': name, 'type': []}]
    response = make_query(query)
    s = set()
    for l in response['result']:
        for topic in l['type']:
            s.add(topic)
    return s
def intersect_types(s1, s2):
    return s1.intersection(s2)
# s1 = get_types('superman')
# s2 = get_types('batman')
# print(intersect_types(s1, s2))

def get_athlete_info(name):
    query = [{'name': name,
              "type": "/sports/pro_athlete",
              "teams": [{
                "team": None,
                "position": [],
                "number": None
              }],
              "sports_played": [{
                "sport": None
              }]
            }]
    return make_query(query)

def make_query(query):
    params = {'query': json.dumps(query), 'key': api_key}
    url = service_url + '?' + urllib.parse.urlencode(params)
    return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

def get_common_types(name1, name2):
    return intersect_types(get_types(name1), get_types(name2))

# print(get_athlete_info('colin kaepernick'))
