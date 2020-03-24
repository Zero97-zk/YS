import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render

def test(request):
    return JsonResponse({'code': 200})