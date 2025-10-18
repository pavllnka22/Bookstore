import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from authentication.views import User

@pytest.fixture
def UserModel():
    """Фікстура для отримання моделі користувача"""
    return get_user_model()

@pytest.fixture(scope='function')
def api_client() -> APIClient:

    return APIClient()

@pytest.fixture(scope='function')
def global_user():

    def create_user(**kwargs):
        defaults = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)
    return create_user

@pytest.fixture
def user_data():

    return {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'NewPass123!',
        'password_check': 'NewPass123!',
        'first_name': 'New',
        'last_name': 'User'
    }
@pytest.fixture

def test_user(django_user_model):
    return django_user_model.objects.create_user(
        username='testuser',
        password='TestPass123!'
    )

@pytest.fixture
def login_data():
    return {
        "username": "testuser",
        "password": "TestPass123!"
    }

@pytest.fixture
def weak_user_data():
    return {
        'username': 'testuser',
        'password': 'testtest'
    }