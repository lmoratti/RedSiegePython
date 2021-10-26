import requests
import sys

def checkSTS(response):
	value = response.headers.get('Strict-Transport-Security')
	
	if value != None:
		print("[Pass]    " +response.url+ " has an STS Header")
		print("    "+str(response.raw._connection.sock.getpeername()[0]))
		return True
	print("[Fail]    " +response.url + " has NO STS Header")
	print("    "+str(response.raw._connection.sock.getpeername()[0]))
	return False
#take commandline arguments
print("Usage: driver.py [Resource: URL of host OR filename] [isFile: expected 0 or 1]")
resource = sys.argv[1]
isFile = sys.argv[2] # 0 if cmd provided host, 1 if file with hosts


if isFile == "0":
	#we add stream = True to be able to grab the IP for Intermediate Task
	response = requests.get(resource,stream=True)
	checkSTS(response)

if isFile =="1":
	# Using readlines()
	file1 = open(resource, 'r')
	lines = file1.readlines()
	 
	for line in lines:
		line= line.rstrip()
		#we add stream = True to be able to grab the IP for Intermediate Task
		response = requests.get(line,stream=True)
		checkSTS(response)




