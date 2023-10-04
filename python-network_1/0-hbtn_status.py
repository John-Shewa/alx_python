#!/usr/bin/python3
""" A script that fetches the url https://alu-intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen("https://alu-intranet.hbtn.io/status") as response:
        html = response.read()
        print('Body response:')
        print('\t - type: {}'.format(type(html)))
        print('\t - content: {}'.format(html))