from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def hello_world(request: HttpRequest):
    context = {"message": "Allah is almighty"}
    rendered = render(request, "index.html", context)
    return HttpResponse(rendered)

