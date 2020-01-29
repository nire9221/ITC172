from django.shortcuts import render
from .models import Meeting, Meeting_Minutes, Resource, Event


# Create your views here.
def index(request):
    return render(request, 'clubApp/index.html')


def gettypes(request):
    type_list = Meeting.objects.all()
    return render(request, 'clubApp/types.html', {'type_list': type_list})
