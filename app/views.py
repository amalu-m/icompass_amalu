from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.exceptions import APIException
import re
#import pdb

@csrf_exempt #disabling in development/Postman
def inputData(request):
    pattern = '(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})'

    #only consider POST requests (per requirement)
    if request.method =='POST':
        #get value for key = 'payload'
        query = request.POST.get('payload', None)
        if query is None:
            raise APIException("There was a problem with input data")

        #check for sql commands using regex
        match = re.search(pattern, query, flags=re.IGNORECASE)
        response = {}
        #check if there are any matches
        if match is None:
            response['result'] = 'sanitized'
        else:
            response['result'] = 'unsanitized'

        #return response
        return JsonResponse(response)
