from django.http import JsonResponse
from uuid import uuid4
from datetime import datetime

def create_uuid():
    return str(uuid4())

def create_datetime():
    return datetime.now()

def create_message(time: datetime):
    # if evening, return 'Good evening'
    # if morning, return 'Good morning'
    # if afternoon, return 'Good afternoon'
    if 6 <= time.hour < 12:
        return 'Good morning'
    elif 12 <= time.hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'

def say_hello(request):
    uuid = create_uuid()
    time = create_datetime()
    message = create_message(time)
    response = {
        'uuid': uuid,
        'datetime': str(datetime.now()),
        'message': message
    }
    return JsonResponse(response)