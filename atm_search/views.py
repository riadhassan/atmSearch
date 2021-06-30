from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from data.atms import get_locations


def hello_world(request: HttpRequest):
    query_location = request.GET.get("location")
    if query_location:
        atms = filter(lambda atm: query_location.lower() in (atm.address+atm.location).lower(), get_locations())
    else:
        atms = get_locations()

    context = {"atm_lists": atms}
    rendered = render(request, "index.html", context)
    return HttpResponse(rendered)

