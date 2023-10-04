#!/usr/bin/python3
""" A script that fetches the url https://alu-intranet.hbtn.io/status"""
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)