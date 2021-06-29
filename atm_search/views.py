from django.http import HttpResponse, HttpRequest


def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Allah is almighty</h1>")

