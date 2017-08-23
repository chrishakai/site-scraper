#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
import urllib2,cookielib
from bs4 import BeautifulSoup, SoupStrainer
sitemap= 'https://www.hakaimagazine.com/sitemap.xml'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Get the sitemap
req = urllib2.Request(sitemap, headers=hdr)
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

# Parse the links out of the site map
for link in BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer('loc')):
    # Get the file location
    m = re.search('http:\/\/www.hakaimagazine.com\/([\w-]+)?\/?([\w-]+)?', link.string)

    # Create the folder structure
    directory = 'downloads'
    if m.group(1) is not None:
        directory += '/' + m.group(1)
    if m.group(2) is not None:
        directory += '/' + m.group(2)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Request the page
    req = urllib2.Request(link.string, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    # Write the file
    contents = open(directory + '/contents.html', 'w')
    contents.write(page.read())
    contents.close()

    # Take a nap so we don't overload the server with many many requests
    time.sleep(0.5)
