import os
import sys
import requests
import json
print("To use this script, first argument should be the API key you're using for ipgeolocation.io.")
print("The second argument should be the individual IP you're looking for, in IPv4 notation.")
print("Since you are passing these via the commandline, an attacker with local access to your machine might be able to look at your bash history to see what IP addresses you've looking at")




print ("Full Argument List: ", str(sys.argv))
apikey = sys.argv[1]
ip = sys.argv[2]

r = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=%s&ip=%s' % (apikey,ip))
#take the response, load it into json so we can pretty print
response = json.loads(r.text)

print(json.dumps(response, indent=4, sort_keys=True))