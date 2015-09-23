from unittest import TestCase
from unittest.mock import Mock

from recipecrawler.client import Client

class TestClient(TestCase):
    HTML_DOC = '<html></html>'
    COOKIE_VALUE = 'persistant_customer_token=12345'
    client = None

    def setUp(self):
        # Create Mock for requests object
        response_for_get = Mock(text=self.HTML_DOC)
        response_for_post = Mock(headers={'set-cookie': self.COOKIE_VALUE})
        requests = Mock(
            **{
                'get.return_value': response_for_get, 
                'post.return_value': response_for_post
            }
        )

        self.client = Client('username', 'password', 'domain')
        self.client.setRequests(requests)

    def test_request(self):
        self.assertEqual(self.client.request('/whatever/'), '<html></html>')

    def test_getSessionId(self):
        self.assertEqual(self.client.getSessionId(), '12345')