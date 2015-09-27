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
        recipeExpected = {'ingredients':['apples', 'bananas', 'pears']}
        recipeMock = Mock(**{'to_json.return_value': recipeExpected})
        recipeFactoryMock = Mock(**{'from_html.return_value': recipeMock})
        clientMock = Client(**self.attrs)
        clientMock.request = MagicMock(return_value='<html></html>')

        crawler = Crawler(clientMock)
        crawler.recipe_factory = recipeFactoryMock

        recipe = crawler.getSingleMenu('/test/path')
        expected = recipe.to_json()

        self.assertEqual(recipeExpected, expected)

        clientMock.request.assert_called_with('/test/path')
        recipeFactoryMock.from_html.assert_called_with('<html></html>')
        recipeFactoryMock.to_json.assert_called()