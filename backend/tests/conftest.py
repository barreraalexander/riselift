from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from server.database import Base, get_db
from server import create_app
from server.config import settings
from server.oauth2 import create_access_token
from server import models, schemas

from secrets import token_hex

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = create_app()
client = TestClient(app)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()


    app = create_app()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user2(client):
    user_data = {
        "name" : "jane",
        "email" : "sheik123@gmail.com",
        "password" : "password234" 
    }
    res = client.post("/users/", json=user_data)

    new_user = schemas.User_MinData(**user_data)
    
    new_user.id = res.json()['id']
    # new_user.id = 10

    assert new_user.email == f'sheik123@gmail.com'
    assert res.status_code == 201
    return new_user



@pytest.fixture
def test_user(client):
    user_data = {
        "name" : "alex",
        "email" : "sheik@gmail.com",
        "password" : "password234" 
    }

    res = client.post("/users/", json=user_data)

    new_user = schemas.User_MinData(**user_data)
    
    new_user.id = res.json()['id']

    assert new_user.email == f'sheik@gmail.com'
    assert res.status_code == 201
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({
        "user_id" : test_user.id,
    })


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture
def test_worksessions(test_user, session, test_user2):
    worksessions_data = [
        {
            'name' : 'workout 1',
            'owner_id' : test_user.id
        },
        {
            'name' : 'workout 2',
            'owner_id' : test_user.id
        },
        {
            'name' : 'workout 3',
            'owner_id' : test_user.id
        },
        {
            'name' : 'workout 1',
            'owner_id' : test_user2.id
        },
        {
            'name' : 'workout 2',
            'owner_id' : test_user2.id
        },

    ]

    def create_worksession_model(work_session):
        return models.WorkSession(**work_session)


    worksession_map = map(create_worksession_model, worksessions_data)
    # print (worksession_map)
    worksessions = list(worksession_map)

    session.add_all(worksessions)
    session.commit()
    
    worksessions = session.query(models.WorkSession).all()

    return worksessions



@pytest.fixture
def test_exercises(test_worksessions, test_user, session):
    exercises_data = [
        {
            'name': 'exercise1',
            'list_index': 0,
            'rep_count': 10,
            'weight': 105,
            'weight_type': 'lbs',
            'owner_id' : test_user.id,
            'worksession_id' : test_worksessions[0].id
        }
    ]

    def create_exercise_model(exercise):
        return models.Exercise(**exercise)

    exercise_map = map(create_exercise_model, exercises_data)
    exercises = list(exercise_map)

    session.add_all(exercises)
    session.commit()

    exercises = session.query(models.Exercise).all()

    return exercises
