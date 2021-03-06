import bs4

from recipe import Recipe, RecipeFactory

class Crawler:
    client = None
    scrapper = None
    recipe_factory = None

    def __init__(self, client):
        self.client = client
        self.scrapper = bs4.BeautifulSoup
        self.recipe_factory = RecipeFactory()

    def getSingleMenu(self, path):
        menuPage = self.client.request(path)
        recipe = self.recipe_factory.from_html(menuPage)
        return recipe

    def getMenuPaths(self, limit=10, offset=0):
        # TODO: An exception should be triggered if client can connect

        path = '/mina-sidor/menyblad-recept?limit=%s&offset=%s' % (limit, offset)
        menusPage = self.client.request(path)
        soup = self.scrapper(menusPage, 'html.parser')
        linksObjs = soup.select('div.menu-recipes a[href^="/mina-sidor/recept/"]')
        paths = [link.attrs.get('href') for link in linksObjs]
        return paths