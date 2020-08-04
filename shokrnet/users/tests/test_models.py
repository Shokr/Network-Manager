import pytest

from shokrnet.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    if user.get_absolute_url() != f"/users/{user.username}/":
        raise AssertionError
