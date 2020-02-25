from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getminutes/', views.getminutes, name='minute'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('getresource/', views.getresource, name='resource'),
    path('newResource/', views.newResource, name='newresource'),
    path('getevent', views.getevent, name='event'),
    path('newEvent/', views.newEvent, name='newevent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
