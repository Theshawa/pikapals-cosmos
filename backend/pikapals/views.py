import json

from django.core.exceptions import BadRequest
from django.http import HttpResponse, HttpRequest

from backend.pikapals.models import Port


def index(_):
    return HttpResponse("Hello, world")


def port_endpoint(request: HttpRequest):
    response: HttpResponse = HttpResponse("")
    if request.method == "GET":
        response: HttpResponse = _port_get(request)
    elif request.method == "POST":
        response: HttpResponse = _port_post(request)
    elif request.method == "UPDATE":
        response: HttpResponse = _port_update(request)
    elif request.method == "DELETE":
        response: HttpResponse = _port_delete(request)

    return response


def _port_post(request: HttpRequest) -> HttpResponse:
    post_data = request.POST
    if "name" not in post_data.keys():
        raise BadRequest("name is required")

    new_port = Port(name=post_data["name"])
    new_port.save()

    data = {"is_success": True, "data": new_port.to_data()}
    return HttpResponse(json.dumps(data))


def _port_get(request: HttpRequest) -> HttpResponse:
    pass


def _port_update(request: HttpRequest) -> HttpResponse:
    pass


def _port_delete(request: HttpRequest) -> HttpResponse:
    pass
