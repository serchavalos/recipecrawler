from unittest import TestCase
from unittest.mock import Mock

from recipecrawler.client import Client

class TestClient(TestCase):
    HTML_DOC = b'<html></html>'
    COOKIE_VALUE = '12345'
    client = None

    def setUp(self):
        self.client = Client('username', 'password', 'domain')
        mockConn = self.__get_connection_mock()
        self.client.setConn(mockConn)

    def tearDown(self):
        None

    def test_request(self):
        self.assertEqual(self.client.request('/whatever/'), '<html></html>')

    def test_getSessionId(self):
        self.assertEqual(self.client.getSessionId(), '12345')

    def __get_connection_mock(self):
        attrs = {
            'getheader.return_value': 'persistant_customer_token=%s;' % self.COOKIE_VALUE,
            'read.return_value': self.HTML_DOC
        }
        mockResponse.Mock(**attrs)

        mockConn = Mock()
        attrs = {'getresponse.return_value': mockResponse}
        mockConn.configure_mock(**attrs)

        return mockConn
