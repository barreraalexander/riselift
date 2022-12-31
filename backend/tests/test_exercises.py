import pytest
from server import schemas

from jose import jwt
from server.config import settings

def test_authorized_get_exercise(authorized_client, test_exercises):
    res = authorized_client.get(f"/exercises/{test_exercises[0].id}")
    assert res.status_code == 200


def test_authorized_get_exercises(authorized_client, test_exercises):
    res = authorized_client.get("/exercises/")
    assert res.status_code == 200

# def test_authorized_user_get_all_exercises(authorized_client):
#     res = authorized_client.get(f"/exercises/")
#     assert res.status_code == 200

# def test_authorized_user_get_one_exercise(authorized_client, test_exercises):
#     res = authorized_client.get(f"/exercises/{test_exercises[0].id}")
#     assert res.status_code == 200

# def test_unauthorized_user_get_all_exercises(client):
#     res = client.get(f"/exercises/")
#     assert res.status_code == 401

# def test_unauthorized_user_get_one_exercise(client, test_exercises):
#     res = client.get(f"/exercises/{test_exercises[0].id}")
#     assert res.status_code == 401

# def test_get_one_exercise_not_exist(authorized_client):
#     res = authorized_client.get(f"/exercises/8888")
#     assert res.status_code == 404


# @pytest.mark.parametrize("name, list_index, rep_count, weight, weight_type, status_code", [
#     ("bench press", 0, 10, 100, 'lbs', 201),
#     ("squat", 1, 1, 400, 'lbs', 201),
#     ("leg press", 2, 16, 47.5, 'lbs', 201),
#     ("shoulder press", 3, 16, 50, 'lbs', 201),
#     ("situps", 4, 16, 0, 'lbs', 201),
# ])
# def test_create_exercises(authorized_client, test_user, test_worksessions,
#     name, list_index, rep_count, weight, weight_type, status_code):

#     res = authorized_client.post(
#         "/exercises/", json={
#             "name": name,
#             "list_index": list_index,
#             "rep_count": rep_count,
#             "weight": weight,
#             "weight_type": weight_type,
#             "worksession_id": test_worksessions[0].id,
#             "owner_id": test_user.id
#         }
#     )

#     created_exercise = schemas.Exercise(**res.json())

#     assert res.status_code == status_code
#     assert created_exercise.name == name

