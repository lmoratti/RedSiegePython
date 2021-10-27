"""This script takes a single host or a file of hosts
 and queries them for basic security headers"""
import sys
import requests

def checkheader(webresponse,header):
    """This function will check a response from a webserver
    for a specific header supplied as a string"""
    value = webresponse.headers.get(header)
    if value is not None:
        print(f"    [Pass]   '{header}'    {value}")
        return True
    print(f"    [FAIL]       NO '{header}' Header Present")
    return False
def checkhost(hostresponse):
    """ This function will check a host for the security
    headers it deems necessary. It takes a webservers response as an argument"""
    ipaddress = hostresponse.raw._connection.sock.getpeername()[0]
    hostname = str(hostresponse.url)
    print(f"    Hostname: {hostname}")
    print(f"    IP: {ipaddress}")
    print("")
    if "https" in hostname:
        checkheader(hostresponse,'Strict-Transport-Security')
    else:
        print("    [FAIL]       Connected over HTTP,ignoring 'Strict-Transport-Security' check")
    checkheader(hostresponse,'Content-Security-Policy')
    checkheader(hostresponse,'X-Frame-Options')
    checkheader(hostresponse,'Server')

#take commandline arguments
print("Usage: driver.py [Resource: URL of host OR filename] [isFile: expected 0 or 1]\n\n\n")
resource = sys.argv[1]
isFile = sys.argv[2] # 0 if cmd provided host, 1 if file with hosts
if isFile == "0":
    #we add stream = True to be able to grab the IP for Intermediate Task
    response = requests.get(resource,stream=True)
    checkhost(response)
if isFile =="1":
    # Using readlines()
    with open(resource, 'r', encoding ='utf-8') as file1:
        lines = file1.readlines()
        print(f"Checking all hosts in {resource} for security headers")
        for line in lines:
            line= line.rstrip() #kept getting a '%0a' newline messing with my files
            #we add stream = True to be able to grab the IP for Intermediate Task
            response = requests.get(line,stream=True)
            checkhost(response)
            print("\n")
