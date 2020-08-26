from django.test import TestCase, RequestFactory
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from accounts.tests.common.mixins import ColumnTestDataMixin
from accounts import views

User = get_user_model()


class ColumnListViewTest(TestCase):
    fixtures = [
        'users.json',
        'columns.json'
    ]

    def test_get_column_list(self):
        # namespace first then name.
        response = self.client.get(reverse("columns:column-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test column")
        self.assertContains(response, "Column list")


class ColumnFeedViewTest(TestCase):
    fixtures = [
        'users.json',
        'columns.json',
        'subscriptions.json'
    ]

    def setUp(self):
        self.factory = RequestFactory()
        self.reader = User.objects.get(email="reader@jd.com")

    def test_get_column_feed(self):
        # test the feed list for a specific user.
        # factory allows us to create a request manually.
        request = self.factory.get(reverse("columns:feed"))
        request.user = self.reader  # assign user
        # request.user = AnonymousUser()
        # import view that handles the request.
        # take view itself and test the way the view is executed.
        # pass the request into the view.
        # passed as a function then we pass request into the function.
        response = views.ColumnFeedView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        # convert from queryset to list.
        column_names = list(request.user.user_subscriptions.all().values_list(
            'column__name', flat=True
        ))
        print(column_names)

        for name in column_names:
            self.assertContains(response, name)


# class DemoTest(TestCase):
#     """
#     setUp
#     setUpClass
#     setUpTestData
#     tearDown
#     tearDownClass
#     """

#     def setUp(self):
#         """Loaded once per test."""
#         # if you have something you need reset for each test case this will be useful.
#         pass

#     def setUpClass(cls):
#         """Once per TestCase class"""
#         pass

#     def setUpTestData(cls):
#         """Once per TestCase class"""
#         pass

#     def test_some_func(self):
#         pass

#     def tearDown(self):
#         pass

#     def tearDownClass(cls):
#         """Once per TestCase class"""
#         pass
