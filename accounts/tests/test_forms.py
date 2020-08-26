from django.test import TestCase
from accounts.models import Column
from accounts.tests.common.mixins import ColumnTestDataMixin
from accounts.forms import PostForm
from django.contrib.auth import get_user_model

User = get_user_model()


class PostFormTest(ColumnTestDataMixin, TestCase):

    def setUp(self):
        self.coordinator = User.objects.get(email="coordinator@test.com")
        self.moderator = User.objects.get(email="moderator@test.com")
        self.writer = User.objects.get(email="writer@test.com")

    def test_post_form(self):
        data = {
            "title": "This is a test post",
            "column": 1
        }

        # only the writer has access to create a post under this column.
        # the above is valid data but the user id is incorrect.
        form = PostForm(data=data, user_id=self.coordinator.id)
        form.is_valid()  # make sure data is valid.
        self.assertTrue(form.errors)

        form = PostForm(data=data, user_id=self.moderator.id)
        form.is_valid()  # make sure data is valid.
        self.assertTrue(form.errors)

        form = PostForm(data=data, user_id=self.writer.id)
        form.is_valid()  # make sure data is valid.
        # the writer has access to create a post on this column
        self.assertFalse(form.errors)
