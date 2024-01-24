#!/usr/bin/env python3
'''obtain content of url'''
import requests
import redis


def get_page(url: str) -> str:
    '''return content and count'''
    r = redis.Redis()
    if r.exists(f"cache:{url}"):
        return r.get(f"cache:{url}")
    else:
        response = requests.get(url)
        r.set(f"cache:{url}", response.text)
        r.expire(f"cache:{url}", 10)
        return response.text
    