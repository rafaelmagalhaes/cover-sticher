import random
import datetime
import time
from goodreads import client
from django.conf import settings
from django.http import JsonResponse


def process_covers(request):
    name = '*list name*'
    isbns = []
    return JsonResponse({
        "count": len(isbns),
        "name": name,
        "url": url,
        "created_at": dt}, safe=False)
