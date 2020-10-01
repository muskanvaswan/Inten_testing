from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .utils import calculate

import json

@api_view(['GET', "POST"])
def calculationResult(request):
    # GET REQUEST TO RENDER UI
    if request.method == 'GET':
        return render(request, "basic/calculate.html")
    # GET REQUEST TO RENDER UI

    # POST METHOD
    if request.method == 'POST':

        # read request data
        request_data = request.data
        decode_request_data = json.dumps(request.data)
        requestDataJson = json.loads(decode_request_data)
        # ends here ~ read request data

        # setting values 
        x =  int(requestDataJson['x'])
        n =  int(requestDataJson['n'])

        # evaluating result to print
        result = calculate(x, n)

        messageData = {'responseType':'success', 'messageType':'success', 'responseData':result}
        respStatusCode = 200
        return JsonResponse(messageData, status=respStatusCode)
