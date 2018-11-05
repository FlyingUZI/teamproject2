from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
# Create your views here.

VERIFICATION_TOKEN = '***********************'


def info(request):
    if request.method != 'POST':
        return JsonResponse({})

    if request.POST.get('token') != VERIFICATION_TOKEN:
        raise SuspiciousOperation('Invalid request.')

    user_name = request.POST['user_name']
    user_id = request.POST['user_id']
