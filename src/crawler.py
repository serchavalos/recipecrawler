class Crawler:
    client = None

    def __init__(self, client):
        self.client = client
        
    def fetchMenuPage(self):
        return self.client.request('/mina-sidor/menyblad-recept')