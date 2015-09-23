from unittest import TestCase
from unittest.mock import MagicMock, Mock

from recipecrawler.client import Client
from recipecrawler.crawler import Crawler

# TODO: update this doesn't apply anymore
class CrawlerTest(TestCase):
    attrs = {
        'username': 'Dummy',
        'password': 'secret',
        'domain': 'www.dummy.com',
    }

    def test_getMenuPaths(self):
        htmlFixture = """
            <div class="menu-recipes ">
                <a href="/mina-sidor/recept/1">Receipt 1</a>
            </div>
            <div class="menu-recipes ">
                <a href="/mina-sidor/recept/2">Receipt 2</a>
            </div>
            <div class="menu-recipes ">
                <a href="/mina-sidor/recept/3">Receipt 3</a>
            </div>
        """
        clientMock = Client(**self.attrs)
        clientMock.request = MagicMock(return_value=htmlFixture)

        crawler = Crawler(clientMock)
        paths = crawler.getMenuPaths()
        expected = ['/mina-sidor/recept/1','/mina-sidor/recept/2','/mina-sidor/recept/3']

        self.assertEqual(paths, expected)

    def test_getSingleMenu(self):
        htmlFixture = """
        <body>
          <div id="ingredients">
            <ul>
              <li>apples</li>
              <li>bananas</li>
              <li>pears</li>
            </ul>
          </div>
          <div id="ingredients">
            <ul>
              <li>potatoes</li>
              <li>carrots</li>
              <li>onions</li>
            </ul>
          </div>
        </body>
        """
        listFixture = [
            Mock(**{'getText.return_value': 'apples'}),
            Mock(**{'getText.return_value': 'bananas'}),
            Mock(**{'getText.return_value': 'pears'}),
        ]
        soupMock = Mock(**{'select.return_value': listFixture})

        scrapperMock = Mock(return_value=soupMock)

        clientMock = Client(**self.attrs)
        clientMock.request = MagicMock(return_value=htmlFixture)

        crawler = Crawler(clientMock)
        crawler.setScrapper(scrapperMock)

        menuObj = crawler.getSingleMenu('/test/path')
        expected = {'ingredients':['apples', 'bananas', 'pears']}

        self.assertEqual(menuObj, expected)

        clientMock.request.assert_called_with('/test/path')
        scrapperMock.assert_called_with(htmlFixture, 'html.parser')
        soupMock.select.assert_called_with('div#ingredients ul > li')