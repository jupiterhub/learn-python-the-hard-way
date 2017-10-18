from nose.tools import *
from app_simple_upload import app

app.config['TESTING'] = True
# basic test client from Flask
web = app.test_client()

def test_all():
    # follow_redirect (changes url if the page redirects)
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    # use bytes for low-level binary data ie. \x41
    # assert_in  forces this
    assert_in(b"Fill Out This Form", rv.data) # b"" byte string

    data = {'name':'Jupiter',  'greet': 'Hola', 'file': 'cat.jpg'}
    rv = web.post('/hello', follow_redirects=True, data=data)

    assert_in(b"Jupiter", rv.data)
    assert_in(b"Hola", rv.data)
