from django.shortcuts import render
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
    meetingname = get_object_or_404(gettypes, pk=id)
    meetingtime = meetingname.getminutes

    context = {
        'meetingname': meetingname,
        'meetingtime': meetingtime,


    }
    return render(request, 'clubApp/meetingdetail.html', context=context)
