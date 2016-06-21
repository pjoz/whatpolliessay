from unittest import TestCase
from AphExtractor import AphExtractor

class TestAphExtractor(TestCase):

    def setUp(self):
        self.extractor = AphExtractor()
        self.senate_size = 76
        self.lower_house_size = 128

    def tearDown(self):
        self.extractor = None
        self.senate_size = None
        self.lower_house_size = None

    def test_get_lower_house_list(self):
        self.setUp()
        lower_house_list = self.extractor.get_lower_house_list()
        assert len(lower_house_list) == self.lower_house_size
        self.tearDown()

    def test_get_senate_list(self):
        self.setUp()
        senate_list = self.extractor.get_senate_list()
        assert len(senate_list) == self.senate_size
        self.tearDown()

    def test_extract_pollies(self):
        self.setUp()
        polly_list = []
    # TODO: add stubbed data for this test
    #     url = 'http://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results?expand=1&q=&par=-1&ps=12&st=1&mem=1'
        self.extractor._extract_pollies(url,polly_list,'')
        assert len(polly_list) == 12

        self.tearDown()