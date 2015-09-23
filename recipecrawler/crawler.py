import bs4

class Crawler:
    client = None
    scrapper = None

    def __init__(self, client):
        self.client = client
        self.scrapper = bs4.BeautifulSoup

    def getSingleMenu(self, path):
        # TODO: Here is where you create your menu object!!!

        menuPage = self.client.request(path)
        soup = self.scrapper(menuPage, 'html.parser')
        ingredientObjs = soup.select('div#ingredients ul > li')
        ingredients = [obj.getText() for obj in ingredientObjs]

        return {'ingredients': ingredients}

    def getMenuPaths(self):
        menusPage = self.client.request('/mina-sidor/menyblad-recept?limit=10')
        soup = self.scrapper(menusPage, 'html.parser')
        linksObjs = soup.select('div.menu-recipes a[href^="/mina-sidor/recept/"]')
        paths = [link.attrs.get('href') for link in linksObjs]
        return paths

    def setScrapper(self, scrapper):
        """ Used for mocking dependencies """
        self.scrapper = scrapper