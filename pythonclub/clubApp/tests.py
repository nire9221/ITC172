from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event
# Create your tests here.


class Meeting(TestCase):
    def test_string(self):
        type = meetingtype(typename: )
        self.assertEqual(str(type), type.typename)
