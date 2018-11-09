from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
from channels import Group
# Create your views here.
# VERIFICATION_TOKEN = '***********************'


def test(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User']
    }

    return JsonResponse(responseData)


# def ws(request):
#     ws = create_connection("ws://127.0.0.1:9999/")
#     ws.send("Hello, World")
#     time.sleep(1)
#     result = ws.recv()
#     time.sleep(1)
#     ws.close()
#     return JsonResponse({'result': result})


def publish(request):
    msg = request.GET.get('msg', 'null')
    Group("sample").send({"text": msg})

    return HttpResponse("Published!")
