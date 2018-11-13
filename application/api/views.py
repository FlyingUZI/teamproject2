from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
from channels import Group
# Create your views here.
import urllib
import urllib.request
# VERIFICATION_TOKEN = '***********************'


def test(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User']
    }

    return JsonResponse(responseData)


def open(request):
    url = ' http://35.236.39.253/api/publish/?msg=open'
    req = urllib.request.Request(url=url)
    urllib.request.urlopen(req)
    return JsonResponse({'msg': 'send open'})


def opend(request):
    return JsonResponse({'msg': 'door opend'})


def publish(request):
    msg = request.GET.get('msg', 'null')
    Group("sample").send({"text": msg})

    return JsonResponse({'msg': msg})
