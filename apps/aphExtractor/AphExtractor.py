import requests
from lxml import html

from Polly import Polly


class AphExtractor:

    baseUrl = "http://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results?expand=1&q=&par=-1&ps=100&st=1"
    senQuery = "sen=1"
    memQuery = "mem=1"
    malQuery = "gen=1"
    femQuery = "gen=2"

    def __init__(self):
        return

    def get_lower_house_list(self):
        polly_list = []

        #get male lower house pollies
        url = '&'.join([self.baseUrl,self.memQuery,self.malQuery])
        self._extract_pollies(url, polly_list, "House of Representatives")

        #get female lower house pollies
        url = '&'.join([self.baseUrl,self.memQuery,self.femQuery])
        self._extract_pollies(url, polly_list, "House of Representatives")

        return polly_list

    def get_senate_list(self):
        polly_list = []

        url = '&'.join([self.baseUrl,self.senQuery])
        self._extract_pollies(url, polly_list, "Senate")

        return polly_list

    def _extract_pollies(self, url, polly_list, house):
        page = requests.get(url)
        tree = html.fromstring(page.content)

        pollies = tree.xpath('//ul[@class="search-filter-results search-filter-results-thumbnails"]')

        for iterPol in pollies[0].iterchildren():
            url   = iterPol[0][0].values()[0]
            id    = url.split('=')[1]
            name  = iterPol[0].text_content()
            title = ""

            detail_extractor = dict(zip(iterPol[3].xpath('dt/text()'),iterPol[3].xpath('dd/text()')))
            party = detail_extractor['Party']
            seat  = detail_extractor['Member for']
            if 'Title(s)' in detail_extractor:
                title = detail_extractor['Title(s)']

            polly_list.append(Polly(name, id, party, seat, title, url, house))

        return True