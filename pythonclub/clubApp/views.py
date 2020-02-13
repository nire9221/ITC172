from django.shortcuts import render, get_object_or_404
from .models import Meeting, Meeting_Minutes, Resource, Event


# Create your views here.
def index(request):
    return render(request, 'clubApp/index.html')


def gettypes(request):
    type_list = Meeting.objects.all()
    return render(request, 'clubApp/types.html', {'type_list': type_list})


def getminutes(request):
    minute_info = Meeting_Minutes.objects.all()
    return render(request, 'clubApp/minute.html', {'minute_info': minute_info})


def meetingdetail(request, id):

    detail = get_object_or_404(Meeting, pk=id)

    return render(request, 'clubApp/meetingdetail.html', {"detail": detail})


def getresource(request):
    resource_list = Resource.objects.all()
    return render(request, 'clubApp/resource.html', {'resource_list': resource_list})
