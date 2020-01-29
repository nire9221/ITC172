from django.shortcuts import render
from .models import Meeting, Meeting_Minutes, Resource, Event


# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')


def gettypes(request):
    type_list = meetingType.objects.all()
    return render(request, 'clubApp/types.html', {'type_list': type_list})
