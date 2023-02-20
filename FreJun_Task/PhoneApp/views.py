from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#importing models from PhoneApp
from PhoneApp.models import CallList
from PhoneApp.serializers import CallListSerializer

# Create your views here.

@csrf_exempt        #all domain calling
def CallAPI(request, id=0):

    if request.method == "GET":
        calls = CallList.objects.all()
        call_serializer = CallListSerializer(calls, many = True)
        return JsonResponse(call_serializer.data, safe = False)

    elif request.method == "POST":
        call_data = JSONParser().parse(request)
        call_serializer = CallListSerializer(data = call_data)

        if call_serializer.is_valid():
            call_serializer.save()
            return JsonResponse("Added Sucessfully", safe = False)
