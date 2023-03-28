#!/usr/bin/env python3

# Script: Ops 301 Class 12 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/28/23
# Purpose: the purpose is listed above each piece of code.
# Resources: Chatgpt helped me format this script and also explained each line of code. 

import requests

# Prompt user for destination URL and HTTP method
url = input("Enter the destination URL: ")
http_method = input("Select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request details and ask for confirmation
print(f"\nSending {http_method} request to {url}...")
confirmation = input("Do you want to proceed? (y/n): ")

# Perform the request only if user confirms
if confirmation.lower() == "y":
    response = requests.request(http_method, url)

    # Print translated response headers
    for header, value in response.headers.items():
        if header.lower() == "content-type":
            print(f"Content Type: {value}")
        elif header.lower() == "content-encoding":
            print(f"Content Encoding: {value}")
        elif header.lower() == "content-language":
            print(f"Content Language: {value}")
        elif header.lower() == "content-length":
            print(f"Content Length: {value}")
        elif header.lower() == "expires":
            print(f"Expires: {value}")
        elif header.lower() == "last-modified":
            print(f"Last Modified: {value}")
        elif header.lower() == "server":
            print(f"Server: {value}")
        elif header.lower() == "etag":
            print(f"ETag: {value}")
        elif header.lower() == "location":
            print(f"Location: {value}")
        elif header.lower() == "pragma":
            print(f"Pragma: {value}")
        elif header.lower() == "cache-control":
            print(f"Cache-Control: {value}")
        elif header.lower() == "connection":
            print(f"Connection: {value}")
        elif header.lower() == "date":
            print(f"Date: {value}")
        elif header.lower() == "set-cookie":
            print(f"Set-Cookie: {value}")
        elif header.lower() == "vary":
            print(f"Vary: {value}")
        elif header.lower() == "www-authenticate":
            print(f"WWW-Authenticate: {value}")
        else:
            print(f"{header}: {value}")

    # Print response header information
    print(f"\nResponse code: {response.status_code}")
    print("Response headers:")
    print(response.headers)
    print("\nResponse body:")
    print(response.content)
else:
    print("Request cancelled.")
