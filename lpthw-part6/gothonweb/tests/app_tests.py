from nose.tools import *
from app import app

app.config['TESTING'] = True
# basic test client from Flask
web = app.test_client()

def test_index_redirect_to_game():
    # follow_redirect (changes url if the page redirects)
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)

def test_go_to_next_room():
    # follow_redirect (changes url if the page redirects)
    rv = web.get('/', follow_redirects=True)

    data = {'action':'tell a joke'}
    rv = web.post('/game', follow_redirects=True, data=data)

    assert_equal(rv.status_code, 200)
    assert_in(b"Laser Weapon Armory", rv.data)

def test_death():
    # follow_redirect (changes url if the page redirects)
    rv = web.get('/', follow_redirects=True)

    data = {'action':'shoot!'}
    rv = web.post('/game', follow_redirects=True, data=data)

    assert_equal(rv.status_code, 200)
    assert_in(b"You Died!", rv.data)


    data = {'action':'dodge!'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert_equal(rv.status_code, 200)
    assert_in(b"You Died!", rv.data)
