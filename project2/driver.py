import requests
import sys

def checkHeader(response,header):
	value = response.headers.get(header)
	if value != None:
		print("    [Pass]   '%s'    %s" % (header,value))
		return True
	print("    [FAIL]       NO '%s' Header Present" % (header))
	return False

def checkHost(response):
	ip = response.raw._connection.sock.getpeername()[0]
	hostname = str(response.url)
	print("    Hostname: %s"% hostname)
	print("    IP: %s"%ip)
	print("")
	if "https" in hostname:
		checkHeader(response,'Strict-Transport-Security')
	else:
		print("    [FAIL]       Connected over HTTP,ignoring 'Strict-Transport-Security' check")
	checkHeader(response,'Content-Security-Policy')
	checkHeader(response,'X-Frame-Options')
	checkHeader(response,'Server')

#take commandline arguments
print("Usage: driver.py [Resource: URL of host OR filename] [isFile: expected 0 or 1]\n\n\n")
resource = sys.argv[1]
isFile = sys.argv[2] # 0 if cmd provided host, 1 if file with hosts


if isFile == "0":
	#we add stream = True to be able to grab the IP for Intermediate Task
	response = requests.get(resource,stream=True)
	checkHost(response)

if isFile =="1":
	# Using readlines()
	file1 = open(resource, 'r')
	lines = file1.readlines()
	
	print("Checking all hosts in %s for security headers" % resource)
	for line in lines:
		line= line.rstrip() #kept getting a '%0a' newline messing with my files
		#we add stream = True to be able to grab the IP for Intermediate Task
		response = requests.get(line,stream=True)
		checkHost(response)
		print("\n")





