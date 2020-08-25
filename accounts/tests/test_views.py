from django.test import TestCase
from accounts.models import Column
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class ColumnListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        coordinator = User.objects.create_user(
            username="coordinator",
            email="coordinator@test.com",
            password="test1234"
        )
        moderator = User.objects.create_user(
            username="moderator",
            email="moderator@test.com",
            password="test1234"
        )
        writer = User.objects.create_user(
            username="writer",
            email="writer@test.com",
            password="test1234"
        )

        column = Column.objects.create(
            name="Test column",
            coordinator=coordinator
        )
        column.moderators.add(moderator)
        column.writers.add(writer)

    def test_get_column_list(self):
        # namespace first then name.
        response = self.client.get(reverse("columns:column-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test column")
        self.assertContains(response, "Column list")


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
