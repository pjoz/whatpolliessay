from lxml import html
import requests, time, datetime

baseUrl = "http://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results?expand=1&q=&par=-1&ps=100&st=1"
senQuery = "sen=1"
memQuery = "mem=1"
malQuery = "gen=1"
femQuery = "gen=2"

def getPolliesList(url,house):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    pollies = tree.xpath('//ul[@class="search-filter-results search-filter-results-thumbnails"]/text()')
    pollyList = []

    for iterPol in pollies[0].iterchildren():
        polUrl   = iterPol[0][0].values()[0]
        polId    = polUrl.split('=')[1]
        polName  = iterPol[0].text_content()
        polTitle = ""

        detailExtractor = dict(zip(iterPol[3].xpath('dt/text()'),iterPol[3].xpath('dd/text()')))
        polParty = detailExtractor['Party']
        polSeat  = detailExtractor['Member for']
        if 'Title(s)' in detailExtractor:
            polTitle = detailExtractor['Title(s)']

        pollyList.append(polly(polName,polId,polParty,polSeat,polTitle,polUrl,house)

class polly:
    """
    This class defines the structure of each Polly in the database.
    """

    name  = ""
    id    = ""
    party = ""
    seat  = ""
    url   = ""
    title = ""
    house = ""
    lastUpdate = 0

    def __init__(self,name,id,party,seat,title,url,house):
        self.name  = name
        self.id    = id
        self.party = party
        self.seat  = seat
        self.title = title
        self.url   = url
        self.house = house
        lastUpdate = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


