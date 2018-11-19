from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_protect
from channels import Group
# Create your views here.
import urllib
import urllib.request

VERIFICATION_TOKEN = '8OuNRs5pasB91tPkQxUJGxvw'


def test(request):
    responseData = {'text': 'got test'}

    return JsonResponse(responseData)


@csrf_protect
def open(request):
    # if request.POST.get('token') != VERIFICATION_TOKEN:
    #     raise SuspiciousOperation('Invalid request.')

    url = 'http://35.236.39.253/api/publish/?msg=open'
    req = urllib.request.Request(url=url)
    urllib.request.urlopen(req)
    return JsonResponse({'text': 'got request'})


def opened(request):
    url = 'http://35.236.39.253/api/publish/?msg=opened'
    req = urllib.request.Request(url=url)
    urllib.request.urlopen(req)
    return JsonResponse({'text': 'door opened'})


def publish(request):
    msg = request.GET.get('msg', 'null')
    Group("sample").send({"text": msg})

    return JsonResponse({'msg': msg})
