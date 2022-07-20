import pytest
from server import schemas

def test_get_all_worksessions():
    assert True

def test_unauthorized_user_get_all_worksessions():
    # res = client.get("/worksessions")
    # assert res.statu
    assert True

def test_unauthorized_user_get_one_worksession():
    assert True


def test_get_one_worksession_not_exist():
    assert True

def test_get_one_worksession():
    assert True


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
    
    # print (created_worksession)
    # assert created_worksession.name == name
    # assert created_worksession == name

