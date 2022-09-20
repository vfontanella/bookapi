from fastapi.testclient import TestClient
from main import app

def test_create_user_ok():
    client = TestClient(app)

    user = {
        'name': 'joe',
        'surname': 'Doe',
        'email': 'test_user_create@provider.co.uk',
        'username': 'joedoetest',
        'password': 'xyz123$'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data['name'] == user['name']
    assert data['surname'] == user['surname']
    assert data['email'] == user['email']
    assert data['username'] == user['username']

    def test_create_user_duplicate_email():
        client = TestClient(app)

        user = {
            'email': 'test_dup_email@provider.co.uk',
            'username': 'test_dup_email',
            'password': 'dup123'
        }

        response = client.post(
            '/api/v1/user/',
            json=user,
        )
        assert response.status_code == 201, response.text

        user['username'] = 'test_dup_email1'

        response = client.post(
            '/api/v1/user/',
            json=user,
        )
        assert response.status_code == 400, response.text
        data = response.json()
        assert data['detail'] == 'Email already registered'


def test_create_user_duplicate_username():
    client = TestClient(app)

    user = {
        'email': 'test_dup_username@provider.co.uk',
        'username': 'test_dup_username',
        'password': 'dup123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Username already registered'

def test_login():
    client = TestClient(app)

    user = {
        'email': 'test-login@provider.co.uk',
        'username': 'test-login',
        'password': 'login123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    login = {
        'username': 'test-login',
        'password': 'login123'
    }

    response = client.post(
        '/api/v1/login/',
        data=login,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects=True
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data['access_token']) > 0
    assert data['token_type'] == 'bearer'