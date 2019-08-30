from django.http import HttpResponse


def index(request):
    return HttpResponse('This is the polls app index function for views.')
