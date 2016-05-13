from django.http import HttpResponse


def index(request):
    return HttpResponse("User.")

def detail(request, User):
    return HttpResponse("User %s." % User)