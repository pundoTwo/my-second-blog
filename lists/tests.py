from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
smokey = SmokeTest()
smokey.test_bad_maths()