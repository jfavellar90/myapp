from django.test import TestCase

# Create your tests here.
from modulepage.views import build_plain_msg


class ModulePageTestCase(TestCase):
    def setUp(self):
        pass

    def test_blog_message(self):
        built_msg = build_plain_msg('hello')
        self.assertEqual(built_msg, 'Message hello end')
