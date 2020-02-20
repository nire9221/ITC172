from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event
from .views import index, gettypes, getminutes, meetingdetail
from .forms import MeetingForm, ResourceForm, EventForm
from django.urls import reverse
from django.contrib.auth.models import User


# Test Case

class MeetingTest(TestCase):
    def setUp(self):
        test = Meeting.objects.create(meetingtype='project', title='new timetable', meetingdate='2020-10-20',
                                      meetingtime='12:00:02', location='seattle central college', agenda='welcoming new student')
        return test

    def test_string(self):
        test = self.setUp()
        self.assertEqual(str(test.meetingtype), 'project')
        self.assertEqual(str(test.title), 'new timetable')
        self.assertEqual(str(test.meetingdate), '2020-10-20')
        self.assertEqual(str(test.meetingtime), '12:00:02')
        self.assertEqual(str(test.location), 'seattle central college')
        self.assertEqual(str(test.agenda), 'welcoming new student')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


# class ResourceTest(TestCase):
#     def test_string(self):
#         src = Resource(resourceName='resource', resourceType='research',
#                        url='http://www.111222.com', description='computer science')
#         self.assertEqual(str(src), src.resourceName)
#         self.assertEqual(str(src), src.resourceType)
#         self.assertEqual(str(src), src.url)
#         self.assertEqual(str(src), src.description)

#     def test_table(self):
#         self.assertEqual(str(Resource._meta.db_table), 'resource')


# class IndexTest(TestCase):
#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)


# class GetTypesTest(TestCase):
#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('gettypes'))
#         self.assertEqual(response.status_code, 200)

#     def setUp(self):
#         self.u = User.objects.create(username='myuser')
#         self.type = Resource.objects.create(meetingtype='entertain', resourceName='name', resourceType='type',
#                                             dateEntered='2019-04-03', url='http://www.111222.com', userId='User', description='some review')
#         self.meeting.user.add(self.u)

#     def test_meeting_detail_success(self):
#         response = self.client.get(
#             reverse('meetingdetail', args=(self.meeting.id,)))
#         # Assert that self.post is actually returned by the post_detail view
#         self.assertEqual(response.status_code, 200)

#     def test_resource(self):
#         resource = Resource.objects.filter(resource=self.src)
#         self.assertEqual(resource, 2)


# Form Tests

class Meeting_Form_Test(TestCase):
    def test_meetingform_is_valid(self):
        form = MeetingForm(
            data={'meetingtype': "test", 'title': "test server", 'meetingdate': "2020-10-20", 'meetingtime': "12:00:02", 'location': "seattle", 'agenda': "test test"})
        self.assertTrue(form.is_valid())

    def test_meetingform_empty(self):
        form = MeetingForm(data={'meetingtype': ""})
        self.assertFalse(form.is_valid())
