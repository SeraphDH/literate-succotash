from unittest import TestCase
from app import app
from flask import session


class FlaskTests(TestCase):
    def setUp(self):
        self.testClient = app.test_client()
        app.config['TESTING'] = True
    def test_homepage(self):
        with self.testClient:
            result = self.testClient.get('/')
            self.assertTrue(session.get('Conversion')== None)
            self.assertTrue(session.get('s')== None)
            self.assertIn(b'Convert From:', result.data)
            self.assertIn(b'Convert To:', result.data)
            self.assertIn(b'Amount', result.data)

    def test_flashmsg(self):
        with self.testClient:
            result = self.testClient.post('/', data=dict(
                currency_from = '',
                currency_to = '',
                ammount = ''
            ))
            self.assertIn(b'is not a valid currency.', result.data)
            self.assertIn(b'is not a valid conversion.', result.data)
            self.assertIn(b'is not a valid amount.', result.data)

    def test_conversion(self):
        with self.testClient:
            result = self.testClient.post('/', data=dict(
                currency_from = 'USD',
                currency_to = 'USD',
                ammount = '1'
            ))
            self.assertIn(b'<b>New Amount:</b> $1.00', result.data)
