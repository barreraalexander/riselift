from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from server.database import Base, get_db
from server import create_app
from server.config import settings
from server.oauth2 import create_access_token
from server import models

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
        "email" : "sheik123@gmail.com",
        "password" : "password234" 
    }

    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def test_user(client):
    user_data = {
        "email" : "sheik@gmail.com",
        "password" : "password234" 
    }

    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({
        "user_id" : test_user.get('id'),
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
            'owner_id' : test_user.get('id')
        },
        {
            'name' : 'workout 2',
            'owner_id' : test_user.get('id')
        },
        {
            'name' : 'workout 3',
            'owner_id' : test_user.get('id')
        },
        {
            'name' : 'workout 1',
            'owner_id' : test_user2.get('id')
        },

    ]

    def create_worksession_model(work_session):
        return models.WorkSession(**work_session)

    worksession_map = map(create_worksession_model, worksessions_data)
    worksessions = list(worksession_map)

    session.add_all(worksessions)
    session.commit()
    
    worksessions = session.query(models.WorkSession).all()

    return worksessions



@pytest.fixture
def test_exercises(test_worksessions, session):
    exercises_data = [
        {
            'name': 'exercise1',
            'list_index': 0,
            'rep_count': 10,
            'weight': 105,
            'weight_type': 'lbs',
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
