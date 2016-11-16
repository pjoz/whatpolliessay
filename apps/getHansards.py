#!/usr/bin/env python3

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

def DownloadFile(url):
    local_filename = url.split('/')[-1].split(';')[0]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return

url = 'http://www.aph.gov.au/Parliamentary_Business/Hansard?wc=%(q)s'
payload = {
    'q': '09/05/2011',
}

date = datetime.strptime(payload['q'], "%d/%m/%Y")

while date < datetime.today():
    print(payload['q'])
    r = requests.get(url % payload)

    soup = BeautifulSoup(r.text)

    for link in soup.find_all(title='XML format'):
        print(link.get('href'))
        DownloadFile(link.get('href'))

    date = date + timedelta(days=7)
    payload['q'] = date.strftime("%d/%m/%Y")
