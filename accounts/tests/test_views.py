from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from accounts.tests.common.mixins import ColumnTestDataMixin


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
