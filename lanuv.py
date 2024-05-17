#!/usr/bin/python

# --------------------------------------------
# Web-Scraping, sort-of
# ...my usual overkill: I use mighty tools to do
# only a tiny little thing.
#

from argparse import ArgumentParser
parser = ArgumentParser(description='fetch a temperature from a LANUV station')
parser.add_argument("-v", "--version", action="version", version='Python: %(prog)s (2024)')
parser.add_argument("-s", "--station", action="store",   dest="STATION", type=str,
                    default='Köln Clevischer Ring', help="a station name", required=False)
args = parser.parse_args()

if args.STATION:
    mystation = args.STATION
else:
    mystation = "Köln Clevischer Ring"

# --------------------------------------------
# do it:
#

import re
import requests
from bs4 import BeautifulSoup
URL = "https://www.lanuv.nrw.de/fileadmin/lanuv/luft/immissionen/aktluftqual/eu_wetter_akt.htm"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("td") # find all "<td>" elements

for i in range(len(results)):
        if results[i].text.find(mystation) >= 0:
            print(results[i].text.strip(), ": ", results[i+1].text, "°C", sep='')

# vi:set tabstop=4:tw=0:expandtab: 
