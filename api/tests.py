from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from random import randint
from .models import Snippet

# Create your tests here.

class ModelTestCase(TestCase):
    """
    The for the Snippet model
    """
    def setUp(self):
        """
        Define the test object and variables
        """
        self.user = User.objects.create(username='test_user')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.snippet = Snippet(owner=self.user, code='Just testing things!')

    def test_is_user_snippet_owner_set(self):
        self.assertEqual(str(self.snippet.owner), 'test_user')
        self.assertEqual(self.snippet.owner, self.user)

    def test_model_can_create_snippet(self):
        """
        Test if possible to create an object
        """
        old_count = Snippet.objects.count()
        self.snippet.save()
        new_count = Snippet.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_are_snippet_linked_to_user(self):
        count = randint(1,42)
        for i in range(count):
            new_snippet = Snippet.objects.create(owner=self.user, code='Test n°' + str(i))
            new_snippet.save()
        self.assertEqual(count, Snippet.objects.count())