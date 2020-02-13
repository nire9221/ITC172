from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event
from .views import index, gettypes, getminutes, meetingdetail
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.


class MeetingTest(TestCase):

    def test_string(self):
        type = Meeting(meetingtype='project', title='new timetable',
                       location='seattle central college', agenda='welcoming new student')
        self.assertEqual(str(type), type.meetingtype)
        self.assertEqual(str(type), type.title)
        self.assertEqual(str(type), type.location)
        self.assertEqual(str(type), type.agenda)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class ResourceTest(TestCase):
    def test_string(self):
        src = Resource(resourceName='resource', resourceType='research',
                       url='http://www.111222.com', description='computer science')
        self.assertEqual(str(src), src.resourceName)
        self.assertEqual(str(src), src.resourceType)
        self.assertEqual(str(src), src.url)
        self.assertEqual(str(src), src.description)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GetTypesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('gettypes'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.u = User.objects.create(username='myuser')
        self.type = Resource.objects.create(meetingtype='entertain', resourceName='name', resourceType='type',
                                            dateEntered='2019-04-03', url='http://www.111222.com', userId='User', description='some review')
        self.meeting.user.add(self.u)

    def test_meeting_detail_success(self):
        response = self.client.get(
            reverse('meetingdetail', args=(self.meeting.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)

    def test_resource(self):
        resource = Resource.objects.filter(resource=self.src)
        self.assertEqual(resource, 2)
