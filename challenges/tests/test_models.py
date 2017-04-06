from django.test import TestCase
from model_mommy import mommy
from challenges.models import Challenge


class TestChallenge(TestCase):

    def setUp(self):
        self.challenge = mommy.make(Challenge, title='Chalenge 1')

    def test_challenge_creation(self):
        self.assertTrue(isinstance(self.challenge, Challenge))
        self.assertEqual(self.challenge.__unicode__(), self.challenge.title)
