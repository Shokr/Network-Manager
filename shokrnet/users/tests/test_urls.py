import pytest
from django.urls import resolve, reverse

from shokrnet.users.models import User

pytestmark = pytest.mark.django_db


def test_detail(user: User):
    if (
        reverse("users:detail", kwargs={"username": user.username})
        != f"/users/{user.username}/"
    ):
        raise AssertionError
    if resolve(f"/users/{user.username}/").view_name != "users:detail":
        raise AssertionError


def test_update():
    if reverse("users:update") != "/users/~update/":
        raise AssertionError
    if resolve("/users/~update/").view_name != "users:update":
        raise AssertionError


def test_redirect():
    if reverse("users:redirect") != "/users/~redirect/":
        raise AssertionError
    if resolve("/users/~redirect/").view_name != "users:redirect":
        raise AssertionError
