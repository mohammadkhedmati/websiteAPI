from django.shortcuts import render
from django.http import Http404, request
from django.utils.cache import add_never_cache_headers
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.conf import settings
import json
import time
from .scraper import *

# Create your views here.

@api_view(['GET', 'POST'])
def AllDetails(request):
    try:
        start_time=time.time()
        main_request=json.loads(request.body)
        user_info=AllInfo(main_request)
        end_time=time.time()-start_time
        print(end_time)
        return JsonResponse(user_info,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)