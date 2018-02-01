import requests
import secrets

#api code is in secret file

# gets stories from a particular section of NY times
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/' #this constructs our query, name of section we want, API key we have and put them all together to get the json and return it for us
    extendedurl = baseurl + section + '.json'
    params={'api-key': secrets.nyt_key} #added secrets because that is where our API key is
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories) # should print a big pile of json
