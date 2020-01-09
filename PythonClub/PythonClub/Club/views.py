from django.http import HttpResponse

def index(request):
    output = "Jinyoung"
    return HttpResponse(output)