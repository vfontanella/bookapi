from fastapi.testclient import TestClient
from main import app


def create_user_and_login(username: str):
    client = TestClient(app)

    user = {
        'email': f'{username}@provider.co.uk',
        'username': username,
        'password': 'xyz123$'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )

    login = {
        'username': username,
        'password': 'xyz123$'
    }

    response = client.post(
        '/api/v1/login/',
        data=login,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects=True
    )

    data = response.json()
    return data['access_token']

    def test_create_book_ok():
        token = create_user_and_login('test-user')
        client = TestClient(app)

        book = {
            'title': 'My fake book',
            'author_id': '0001',
            'subject_id': '0001',
            'cover_photo': '',
            'isbn': 'BAS923498747',
            'released_at': '2001',
            'is_lent': 'false'
        }

        response = client.post(
            '/api/v1/book/',
            json=book,
            headers={
                'Authorization': f'Bearer {token}'
            }
        )

        assert response.status_code == 201, response.text
        data = response.json()
        assert data['title'] == book['title']
        assert data['isbn'] == book['isbn']
        assert data['is_lent'] == False

