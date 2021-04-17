

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import requests
import json


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_weather(request):
    try:
        city = request.query_params['city']
        days = request.query_params['days']
        data = give_me_weather(city, days)
        return Response(data)
    except Exception as e:
        return Response({'error':'system error', 'detail': str(e)})


def give_me_weather(city, days):
    if 2 < len(city) < 45:
        api_key = ''
        req = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
        payload = {
            "key": api_key,
            "q": city,
            "format": "json",
            "num_of_days": days,
            "fx": "yes", "mca": "yes","fx24": "no", "show_comments": "no",
            "tp": "12", "showlocaltime": "yes", "lang": "tr", }
        res = requests.get(req, params=payload)
        return json.loads(res.text)
    else:
        return {'error': 'sorry you want too much from me, something must be wrong with city name'}
