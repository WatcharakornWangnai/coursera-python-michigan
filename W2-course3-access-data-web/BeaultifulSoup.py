#using BeautifulSoup for html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)
import re

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
pos = int(input('Enter position: '))
rep = int(input('Enter #repeat: '))
n = 0
while n < rep:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    lst = list()
    for tag in tags:
        x = tag.get('href', None)
        lst.append(x)
    y = lst[pos-1]
    name = re.findall('known_by_([a-zA-Z]+)',y)
    a = name[0]
    n = n + 1
    print(n,a)
    url = y
    
    