#!/usr/bin/python3
""" A script that fetches the url https://alu-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests

    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    if response.status_code == 200:
        print('Body response:')
        print('\t - type: {}'.format(type(url)))
        print('\t - content: {}'.format(requests))