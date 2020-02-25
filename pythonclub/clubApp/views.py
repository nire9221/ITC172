from django.shortcuts import render, get_object_or_404
from .models import Meeting, Meeting_Minutes, Resource, Event
from .forms import MeetingForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required


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


def getevent(request):
    event_list = Event.objects.all()
    return render(request, 'clubApp/event.html', {'event_list': event_list})


def newMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'clubApp/newmeeting.html', {'form': form})


def newResource(request):
    form = ResourceForm
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'clubApp/newresource.html', {'form': form})


def newEvent(request):
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = EventForm()
    else:
        form = EventForm()
    return render(request, 'clubApp/newevent.html', {'form': form})


def loginmessage(request):
    return render(request, 'clubApp/loginmessage.html')


def logoutmessage(request):
    return render(request, 'clubApp/logoutmessage.html')


@login_required
def newProduct(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'clubApp/newmeeting.html', {'form': form})
