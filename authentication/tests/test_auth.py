import pytest
from rest_framework import status
import logging

logging.disable(logging.CRITICAL)


@pytest.mark.django_db
class TestUser:

    def test_successful_registration(self, api_client, user_data):
        url = '/api/auth/register/'
        response = api_client.post(url, user_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['user']['username'] == 'newuser'

    def test_registration_duplicate_username(self, api_client, test_user, user_data):

        user_data['username'] = test_user.username
        url = '/api/auth/register/'

        response = api_client.post(url, user_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'username' in response.data

    def test_registration_weak_password(self, api_client):

        weak_user_data = {
            'username': 'weakuser',
            'email': 'weak@example.com',
            'password': '123',
            'password_check': '123'
        }
        url = '/api/auth/register/'
        response = api_client.post(url, weak_user_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_registration_missing_username(self, api_client, user_data):

        del user_data['username']
        url = '/api/auth/register/'

        response = api_client.post(url, user_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_registration_missing_email(self, api_client, user_data):

        del user_data['email']
        url = '/api/auth/register/'

        response = api_client.post(url, user_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_registration_password_mismatch(self, api_client, user_data):

        user_data['password_check'] = 'DifferentPass123!'
        url = '/api/auth/register/'

        response = api_client.post(url, user_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestUserLogin:

    def test_successful_login(self, api_client, login_data, test_user):

        url = '/api/auth/login/'
        response = api_client.post(url, login_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_login_wrong_data(self, api_client, test_user):
        url = '/api/auth/login/'
        response = api_client.post(url, {
            'username': 'unknown',
            'password': 'wrong'
        }, format='json')

        print(response.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data['error'] == 'Invalid credentials'


@pytest.mark.django_db
class TestProtectedViews:

    def test_protected_view_unauthenticated(self, api_client):

        url = '/api/auth/protected/'
        response = api_client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
class TestUserLogoutWithFixtures:

    def test_logout_unauthenticated(self, api_client):

        url = '/api/auth/logout/'
        response = api_client.post(url, {}, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

