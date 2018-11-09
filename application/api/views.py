from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
# Create your views here.

# VERIFICATION_TOKEN = '***********************'


def test(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User']
    }

    return JsonResponse(responseData)
