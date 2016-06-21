import datetime
import time


class Polly:
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


if __name__ == '__main__':
    senate_list      = get_senate_list()
    lower_house_list = get_lower_house_list()

    print senate_list