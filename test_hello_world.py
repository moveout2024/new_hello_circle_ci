import hello_world
import unittest

import pytest
from hello_world import app, generate_html, greet

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greet():
    assert greet() == 'Welcome to CI/CD'

def test_generate_html():
    message = 'Test Message'
    version_number = '0001'
    expected_html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="340" width="1200" src="https://user-images.githubusercontent.com/194400/41597205-a57442ea-73c4-11e8-9591-61f5c83c7e66.png">
                <br> {0}
                <p>Version Number: {1}</p>
                <br>
            </div>
        </body>
        </html>""".format(message, version_number)

    assert generate_html(message) == expected_html

def test_hello_world(client):
    response = client.get('/')
    assert b'Welcome to CI/CD' in response.data
    assert b'Version Number: 0001' in response.data
