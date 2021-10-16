import os
import sys
import requests
import json
print("To use this script...")
print("The first argument should be: \n    The API key you're using for ipgeolocation.io.")
print("The second argument should be:\n    '0' if you are giving a single IP via commandline\n    '1' if a file with multiple IPs")
print("The third argument should be:\n    the individual IP you're looking for OR a file name with multiple IPs")
print("WARNING: You are passing info via the commandline. An attacker with local access to your machine might be able to look at your bash history.")
print("In which case, they can see what IP addresses you've been looking at or your API key. OpSec is important, folks.")


def queryIP(resource):
	r = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=%s&ip=%s' % (apikey,resource))
	#take the response, load it into json so we can prettyprint output
	response = json.loads(r.text)
	print(json.dumps(response, indent=4, sort_keys=True))



apikey = sys.argv[1]
isFile = sys.argv[2] #check flag if specifying a file
resource = sys.argv[3] 

#option for single IP passed in
if isFile == "0":
	queryIP(resource)

#option for file with multiple IPs passed in
if isFile == "1":
	# Using readlines()
	file1 = open(resource, 'r')
	lines = file1.readlines()
	 
	for line in lines:
	    queryIP(line)

if isFile != "0" and isFile != "1":
	print("The second argument should be a '0' if you are giving a single IP, '1' if a file with multiple IPs")
	#Could optionally throw an exception here
