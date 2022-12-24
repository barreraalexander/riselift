import pytest
from server import schemas
from jose import jwt
from server.config import settings

def test_create_user(client):
    res = client.post("/users/", json={
        "name" : "alex",
        "email" : f'test_user@gmail.com',
        "password" : 'password123'
    })

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == f'test_user@gmail.com'
    # assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post("/login", data={
        "name" : "alex",
        "username" : test_user['email'],
        "password" : test_user['password']
    })

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])

    id = payload.get('user_id')

    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    # assert res.status_code == 200

# @pytest.mark.parametrize("email, password, status_code", [
#     ('wrongemail@gmail.com', 'password123', 403),
#     ('barrera93@gmail.com', 'wrongpassword', 403),
#     ('wrongemail@gmail.com', 'wrongpassword', 403),
#     (None, 'password123', 422),
#     ('sanjeez@gmail.com', None, 422)
# ])
# def test_incorrect_login(client, email, password, status_code):
#     res = client.post("/login", data={
#         "username" : email,
#         "password" : password,
#     })

#     assert res.status_code == status_code