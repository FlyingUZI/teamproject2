from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
# Create your views here.

VERIFICATION_TOKEN = '***********************'


def test(request):
    json = serializers.serialize('json', {"description": "\u307b\u3052\u307b\u3052\uff01", "created": "2010-11-17 21:21:01",
                                          "modified": "2010-11-17 21:21:01", "summary": "\u3042\u305a\u306b\u3083\u3093\uff01", "name": "azunyan"}, ensure_ascii=False)
    return HttpResponse(json, mimetype='application/json')
