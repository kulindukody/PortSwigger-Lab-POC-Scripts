import argparse
import requests
import subprocess, os
import string

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    #parser.add_argument("--", required=True, help="")
    parser.add_argument("--user", required=True, help="The users account to take over")
    parser.add_argument("--url", required=True, help="URL of the victim application")
    parser.add_argument("--ip", help="IPv4 of your local machine for reverse shell.")
    parser.add_argument("--port", help="Port for reverse shell")
    parser.add_argument("--proxy", help='proxy everything through burp', action='store_true', default=False)
    parser.add_argument("--debug", action='store_true', default=False, help='Enable debugging output')
    args = parser.parse_args()

    url = args.url.rstrip('/')
    print(url)
