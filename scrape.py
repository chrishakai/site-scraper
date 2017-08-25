#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
import urllib2,cookielib
from bs4 import BeautifulSoup, SoupStrainer
sitemap= 'https://www.hakaimagazine.com/sitemap.xml'
#sitemap= 'http://localhost/sitemap_one.xml'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Get the sitemap
print '\033[92m' + 'Getting ' + sitemap + '\033[0m'
req = urllib2.Request(sitemap, headers=hdr)
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()
print '\033[91m' + '-----------------------------------------------------' + '\033[0m'
# Parse the links out of the site map

links = BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer('loc'))
for idx, link in enumerate(links):
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
    if not os.path.exists(directory + '/img'):
        os.makedirs(directory + '/img')

    # Request the page
    req = urllib2.Request(link.string, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    # Write the file
    print '\033[92m' + 'Starting page ' + directory + '\033[0m'
    htmlpage = page.read()
    soup = BeautifulSoup(htmlpage, 'html.parser')

    # Request source images
    imglinks = soup.find_all('source')
    imgfiles = []
    for image in imglinks:
        imgname = re.search('https:\/\/www.hakaimagazine.com\/sites\/default\/files\/styles\/[\w]+\/[\w]+\/([-\w.\/]+)', image.get('srcset').split(',')[0])
        imgfiles.append(imgname.group(1))
    imgfiles = list(set(imgfiles))
    for image in imgfiles:
        imagename = re.search('(?:.+\/)*([-\w]+\..+)', image).group(1)
        f = open(directory + '/img/' + imagename,'wb')
        print 'Write image ' + '\033[94m' + directory + '/img/' + imagename + '\033[0m'
        req = urllib2.Request('https://www.hakaimagazine.com/sites/default/files/' + image, headers=hdr)
        f.write(urllib2.urlopen(req).read())
        f.close()
    # Request twitter images

    # Request facebook images

    # Write the file
    contents = open(directory + '/contents.html', 'w')
    print 'Write file ' + '\033[94m' + directory + '/contents.html' + '\033[0m' + ': ' + '\033[93m' + htmlpage[:15] + '\033[0m'
    contents.write(htmlpage)
    contents.close()
    print '\033[91m' + str(idx + 1) + ' of ' + str(len(links)) + ' done -----------------------------------------------------' + '\033[0m'
    # Take a nap so we don't overload the server with many many requests
    time.sleep(0.5)
