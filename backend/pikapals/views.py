import json

from django.core.exceptions import BadRequest
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from pikapals.models import Port, ServiceProvider


def index(_):
    return HttpResponse("Hello, world")


@csrf_exempt
def port_endpoint(request: HttpRequest):
    response: HttpResponse = HttpResponse("")
    if request.method == "GET":
        response: HttpResponse = _port_get(request)
    elif request.method == "POST":
        response: HttpResponse = _port_post(request)
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
    get_data = request.GET
    if "id" not in get_data.keys():
        # return all ports
        ports = Port.objects.all()
        data = {"is_success": True, "data": [port.to_data() for port in ports]}
        return HttpResponse(json.dumps(data))

    try:
        port = Port.objects.get(id=get_data["id"])
    except Port.DoesNotExist:
        return HttpResponseNotFound()

    data = {"is_success": True, "data": port.to_data()}
    return HttpResponse(json.dumps(data))


def _port_delete(request: HttpRequest) -> HttpResponse:
    delete_data = request.POST
    if "id" not in delete_data.keys():
        raise BadRequest("id is required")

    port = Port.objects.get(id=delete_data["id"])
    port.delete()

    data = {"is_success": True}
    return HttpResponse(json.dumps(data))


@csrf_exempt
def service_provider_endpoint(request: HttpRequest):
    response: HttpResponse = HttpResponse("")
    if request.method == "GET":
        response: HttpResponse = _service_provider_get(request)
    elif request.method == "POST":
        response: HttpResponse = _service_provider_post(request)
    elif request.method == "DELETE":
        response: HttpResponse = _service_provider_delete(request)

    return response


def _service_provider_post(request: HttpRequest) -> HttpResponse:
    post_data = request.POST
    if "name" not in post_data.keys():
        raise BadRequest("name is required")

    new_service_provider = ServiceProvider(name=post_data["name"])
    new_service_provider.save()

    data = {"is_success": True, "data": new_service_provider.to_data()}
    return HttpResponse(json.dumps(data))


def _service_provider_get(request: HttpRequest) -> HttpResponse:
    get_data = request.GET
    if "id" not in get_data.keys():
        # return all service_providers
        service_providers = ServiceProvider.objects.all()
        data = {"is_success": True, "data": [service_provider.to_data() for service_provider in service_providers]}
        return HttpResponse(json.dumps(data))

    try:
        service_provider = ServiceProvider.objects.get(id=get_data["id"])
    except ServiceProvider.DoesNotExist:
        return HttpResponseNotFound()

    data = {"is_success": True, "data": service_provider.to_data()}
    return HttpResponse(json.dumps(data))


def _service_provider_delete(request: HttpRequest) -> HttpResponse:
    delete_data = request.POST
    if "id" not in delete_data.keys():
        raise BadRequest("id is required")

    service_provider = ServiceProvider.objects.get(id=delete_data["id"])
    service_provider.delete()

    data = {"is_success": True}
    return HttpResponse(json.dumps(data))
