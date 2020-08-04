import pytest
from django.test import RequestFactory

from shokrnet.users.models import User
from shokrnet.users.views import UserRedirectView, UserUpdateView

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    @staticmethod
    def test_get_success_url(user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        if view.get_success_url() != f"/users/{user.username}/":
            raise AssertionError

    @staticmethod
    def test_get_object(user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        if view.get_object() != user:
            raise AssertionError


class TestUserRedirectView:
    @staticmethod
    def test_get_redirect_url(user: User, rf: RequestFactory):
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        if view.get_redirect_url() != f"/users/{user.username}/":
            raise AssertionError
