import json
from typing import List, Tuple

from django.core.exceptions import BadRequest
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from pikapals.models import Port, ServiceProvider, Voyage


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


@csrf_exempt
def voyage_endpoint(request: HttpRequest) -> HttpResponse:
    response: HttpResponse = HttpResponse("")
    if request.method == "GET":
        response: HttpResponse = _voyage_get(request)
    elif request.method == "POST":
        response: HttpResponse = _voyage_create(request)
    return response


def _voyage_get(request: HttpRequest):
    get_data = request.GET
    if "voyage_no" not in get_data.keys():
        voyages = Voyage.objects.all()
        data = {"is_success": True, "data": [voyage.toData() for voyage in voyages]}
        return HttpResponse(json.dumps(data))
    voyage_no = get_data["voyage_no"]
    try:
        voyage = Voyage.objects.get(voyage_no=voyage_no)
    except Voyage.DoesNotExist:
        return HttpResponseNotFound()
    return HttpResponse(json.dumps({"is_success": True, "data": voyage.toData()}))


def _voyage_create(request: HttpRequest):
    try:
        post_data = request.POST
        if "voyage_no" not in post_data.keys():
            raise BadRequest("voyage_no is required")
        if "service_provider_id" not in post_data.keys():
            raise BadRequest("service_provider_id is required")
        if "start_port_id" not in post_data.keys():
            raise BadRequest("start_port_id is required")
        if "destination_port_id" not in post_data.keys():
            raise BadRequest("destination_port_id is required")

        voyage_no = post_data["voyage_no"]
        service_provider = ServiceProvider.objects.get(id=post_data["service_provider_id"])
        start_port = Port.objects.get(id=post_data["start_port_id"])
        destination_port = Port.objects.get(id=post_data["destination_port_id"])
        new_voyage = Voyage(voyage_no=voyage_no, service_provider=service_provider, start_port=start_port,
                            destination_port=destination_port)
        new_voyage.save()

        # add seats
        if "seats" in post_data.keys() and type(post_data["seats"]) is List[Tuple['SeatClass', int, int]]:
            new_voyage.create_seats(post_data["seats"])

        data = {"is_success": True, "data": new_voyage.to_data()}
        return HttpResponse(json.dumps(data))

    except ServiceProvider.DoesNotExist or Port.DoesNotExist:
        return HttpResponseNotFound()
