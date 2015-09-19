from unittest import TestCase
from unittest.mock import MagicMock

from recipecrawler.client import Client
from recipecrawler.crawler import Crawler

class CrawlerTest(TestCase):

    def test_fetchMenuPage(self):
        attrs = {
            'username': 'Dummy',
            'password': 'secret',
            'domain': 'www.dummy.com',
        }
        clientMock = Client(**attrs)
        clientMock.request = MagicMock(return_value='<html></html>')

        crawler = Crawler(clientMock)
        self.assertEqual(crawler.fetchMenuPage(), '<html></html>')
