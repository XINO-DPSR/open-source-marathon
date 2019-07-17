# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import search_database
import json
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Defining home page


def home(request):
    return render(request, 'src/index.html')

# Searching at every post request


def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_string = data.get('query', None)
        records = search_database.objects.values_list('query', flat=True)
        records = list(records)
        result = []
        for i in records:
            if search_string.lower() in i.lower():
                result.append(i)
        return JsonResponse({'query': result})
