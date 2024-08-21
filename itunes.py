import json
import requests
import sys

#if the user dont make any good search, exit
if len(sys.argv) != 2:
    sys.exit()#end the progam
   #elif if the user find or request a song that is in itunes, get a response  
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#its going to be formated in JSON a language that is for all the computers language
#json.dumps its to convert the JSON language in a more smoothy way to convert my information
#print(json.dumps(response.json(), indent=2))
#indent to make spaces

o = response.json()#HERE im looking in response of JSON, and getting to o
#its to fin in the same dictionary the part of the JSON file that have "trackName"
for result in o["results"]:#"results" its a list
    print(result["trackTimeMillis"])
    
    
    
    
    #API is the Word for searching in URL something