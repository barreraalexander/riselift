import pytest
from server import schemas
from jose import jwt
from server.config import settings

from secrets import token_hex

def test_create_user(client):
    rand = token_hex(5)

    res = client.post("/users/", json={
        "email" : f'test_user_{rand}@gmail.com',
        "password" : 'password123'
    })

    # new_user = schemas.UserOut(**res.json())
    # print (new_user)
    # assert new_user.email == f'test_user_{rand}@gmail.com'
    # assert res.status_code == 201
    print (res.json())

def test_get_root(client):
    res = client.get("/")
    print (res.json())
    assert True

def test_login_user():
    assert True