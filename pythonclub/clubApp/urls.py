from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getminutes/', views.getminutes, name='minute'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
]
