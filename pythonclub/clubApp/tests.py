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


class ResourceTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='newnew', password='what')

        test = Resource.objects.create(resourceName='research', resourceType='essay', url='http://wwww.w3.com',
                                       dateEntered='2020-10-20', userId=self.test_user, description='seattle central college')
        return test

    def test_string(self):
        test = self.setUp()
        self.assertEqual(str(test.resourceName), 'research')
        self.assertEqual(str(test.resourceType), 'essay')
        self.assertEqual(str(test.url), 'http://wwww.w3.com')
        self.assertEqual(str(test.dateEntered), '2020-10-20')
        self.assertEqual(str(test.meetingtime), '12:00:02')
        self.assertEqual(str(test.userId), 'newnew')
        self.assertEqual(str(test.description), 'seattle central college')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


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


class Resource_Form_Test(TestCase):
    def test_resource_user_foreign_key(self):
        self.test_user = User.objects.create_user(
            username='newnew', password='what')

    def test_resourceform_is_valid(self):
        form = ResourceForm(
            data={'resourceName': "test", 'resourceType': "test server",
                  'url': "http://www.w3.com", 'dateEntered': "2020-10-20", 'userId': self.test_user, 'description': "test test"})
        self.assertTrue(form.is_valid())

    def test_resourceform_empty(self):
        form = ResourceForm(data={'resourceName': ""})
        self.assertFalse(form.is_valid())


class Event_Form_Test(TestCase):

    def test_eventform_is_valid(self):
        self.test_user = User.objects.create_user(
            username='newnew', password='what')
        form = EventForm(
            data={'eventTitle': "test", 'location': "test server", 'date': "2020-10-20", 'time': "12:00:02", 'description': "seattle", 'userId': self.test_user})
        self.assertTrue(form.is_valid())

    def test_eventform_empty(self):
        form = EventForm(data={'eventTitle': ""})
        self.assertFalse(form.is_valid())


class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.meeting = Meeting.objects.create(meetingtype='python', title='project', meetingtime='10:20:24',
                                              meetingdate='2019-04-02', location='scc', agenda="project python final")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(
            response, '/accounts/login/?next=/clubApp/newmeeting')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='P@ssw0rd1')
        response = self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clubApp/newmeeting.html')
