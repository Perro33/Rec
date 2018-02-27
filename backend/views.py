from django.shortcuts import render
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

# Create your views here.

@require_http_methods(['GET'])
def get_result(request):
    response = {}
    response['msg'] = "ok"

    return JsonResponse(response)