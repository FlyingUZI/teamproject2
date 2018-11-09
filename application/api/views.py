from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
# Create your views here.

VERIFICATION_TOKEN = '***********************'


def test(request):
    return "test"
