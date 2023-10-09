#!/usr/bin/python3
""" A script that takes in a letter and sends a post request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    qry = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dat = response.json()
        if dat == {}: