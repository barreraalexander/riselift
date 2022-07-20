import pytest
from server import schemas


def test_get_all_worksessions(authorized_client, test_worksessions):
    res = authorized_client.get("/worksessions/")


    # def validate(worksession):
    #     return schemas.WorkSessionOut(**worksession)
    # worksessions_map = map(validate, res.json())
    # worksessions_list = list(worksessions_map)

    # assert len(res.json()) == len(test_worksessions)
    # assert res.status_code == 200
    print (res.json())


def test_unauthorized_user_get_all_worksessions(client, test_worksessions):
    res = client.get("/worksessions/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_worksession(client, test_worksessions):
    res = client.get(f"/worksessions/{test_worksessions[0].id}")
    assert res.status_code == 401

def test_get_one_worksession_not_exist(authorized_client, test_worksessions):
    res = authorized_client.get(f"/worksessions/8888")
    assert res.status_code == 404


def test_get_one_worksession(authorized_client, test_worksessions):
    res = authorized_client.get(f"/worksessions/{test_worksessions[0].id}")
    # worksession = schemas.WorkSessionOut(**res.json())
    # assert worksession.WorkSession.id == test_worksessions[0].id


@pytest.mark.parametrize("name", [
    ("pushups"),
    ("situps"),
    ("abs"),
    ("lunges"),
])
def test_create_worksession(authorized_client, test_user, test_worksessions, name):
    res = authorized_client.post(
        "/worksessions/", json={
            "name" : name
        }
    )

    created_worksession = schemas.WorkSession(**res.json())
    
    assert res.status_code == 201
    assert created_worksession.name == name
    assert created_worksession.owner_id == test_user.get('id')

 
def test_unauthorized_user_create_worksessions(client, test_user, test_worksessions):
    res = client.post(
        "/worksessions/", json={
            "name" : "arbitrary name"
        })
    assert res.status_code == 401


def test_unauthorized_user_delete_post(client, test_user, test_worksessions):
    res = client.delete(
        f"/worksessions/{test_worksessions[3].id}"
    )
    assert res.status_code == 401


def test_delete_post_success(authorized_client, test_user, test_worksessions):
    res = authorized_client.delete(
        f"/worksessions/{test_worksessions[0].id}"
    )

    assert res.status_code == 204

def test_delete_post_non_exist(authorized_client, test_user, test_worksessions):
    res = authorized_client.delete(
        f"/worksessions/9999"
    )

    assert res.status_code == 404

# def test_delete_other_user_post(authorized_client, test_user, test_worksessions):
#     res = authorized_client.delete(
#         f"/worksessions/{test_worksessions[3].id}"
#     )
    
#     assert res.status_code == 403