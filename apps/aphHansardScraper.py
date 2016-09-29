#!/usr/bin/env python

import os
import requests
import wget
from bs4 import BeautifulSoup

aphUrl = "http://www.aph.gov.au/Parliamentary_Business/Hansard"
r = requests.get(aphUrl)
soup = BeautifulSoup(r.content, 'html.parser')

link_list = soup.find_all(title="XML format")

for link in link_list:
    downloadLink = link['href'].split(';')[0]
    filename = wget.download(downloadLink)
    print downloadLink
    print filename
    if filename.startswith("House%20of%20Representatives"):
        os.rename(filename, filename.replace("House%20of%20Representatives", "House-of-Representatives"))
