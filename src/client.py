import re
import pprint

from http.client import HTTPSConnection

class Client:
    conn = None
    params = None
    headers = None
    domain= None
    sessionId = None

    def __init__(self, username, password, domain):
        self.domain = domain
        self.params = 'username={username}&password={password}'.format(username=username, password=password)
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': self.domain,
            'Origin': 'https://' + self.domain,
            'Referer': 'https://' + self.domain,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
        }
        self.conn = HTTPSConnection(self.domain)

    def request(self, uri):
        self.headers['cookie'] = 'persistant_customer_token={id};'.format(id=self.getSessionId())
        self.conn.request('GET', uri, '', self.headers)
        response = self.conn.getresponse()
        html = response.read()
        html = html.decode('utf-8')
        self.conn.close()

        return html

    def getSessionId(self):
        cookies = self._getSessionCookies()
        match = re.search('persistant_customer_token=([^;]+)', cookies)
        if match:
            return match.group(1)

        return None


    def _getSessionCookies(self):
        # return 'PHPSESSID=04g6qe180ibng685h6cq5d3vo3; path=/, persistant_customer_token=8e853fe1ce26bb526f83049b3588f55826e8bda9; expires=Mon, 29-Aug-2016 15:00:53 GMT; Max-Age=31104000; path=/'

        self.conn.request('POST', '/utility', self.params, self.headers)
        response = self.conn.getresponse()
        cookies = response.getheader('Set-Cookie')
        self.conn.close()
        return cookies