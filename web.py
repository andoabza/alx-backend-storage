#!/usr/bin/env python3
'''obtain content of url'''
import requests

def get_page(url: str) -> str:
    r = requests.get('http://slowwly.robertomurray.co.uk')
    return r.content