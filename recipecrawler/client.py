import re, pprint, requests

class Client:
    requests = None
    params = None
    headers = None
    domain= None
    sessionId = None

    def __init__(self, username, password, domain):
        self.domain = domain
        self.requests = requests
        self.params = 'username={username}&password={password}'.format(username=username, password=password)
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': self.domain,
            'Origin': 'https://' + self.domain,
            'Referer': 'https://' + self.domain,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
        }

    def request(self, uri):
        sessionId = self.getSessionId()
        self.headers['cookie'] = 'persistant_customer_token={id};'.format(id=sessionId)

        url = 'https://%s%s' % (self.domain, uri)
        response = self.requests.get(url, headers=self.headers)
        html = response.text

        return html

    def getSessionId(self):
        if self.sessionId is not None:
            return self.sessionId

        cookies = self._getSessionCookies()
        match = re.search('persistant_customer_token=([^;]+)', cookies)
        if match:
            return match.group(1)

        return None

    def setRequests(self, requests):
        """ Used for mocking """
        self.requests = requests

    def _getSessionCookies(self):
        # return 'PHPSESSID=04g6qe180ibng685h6cq5d3vo3; path=/, persistant_customer_token=8e853fe1ce26bb526f83049b3588f55826e8bda9; expires=Mon, 29-Aug-2016 15:00:53 GMT; Max-Age=31104000; path=/'

        url = 'https://%s%s' % (self.domain, '/utility')
        res = self.requests.post(url, data=self.params, json=None, headers=self.headers, allow_redirects=False)

        return res.headers['set-cookie']
