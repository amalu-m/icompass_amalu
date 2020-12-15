from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.exceptions import APIException
import re
import pdb

@csrf_exempt #disabling in development/Postman
def inputData(request):
    #only consider POST requests (per requirement)
    if request.method == 'POST':
        #get value for key = 'payload'
        query = request.POST.get('payload', None)
        if query is None:
            raise APIException("There was a problem with input data")

        hasMatchingPattern = hasSqlInjection(query)
        result = buildResponse(hasMatchingPattern)
        return result

def hasSqlInjection(input):
    pattern = '(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})'
    #check for sql commands using regex
    match = re.search(pattern, input, flags = re.IGNORECASE)
    # pdb.set_trace()
    if match is None:
        return False
    else:
        return True

def buildResponse(hasMatchingPattern):
        response = {}
        #check if there are any matches
        if hasMatchingPattern:
            response['result'] = 'unsanitized'
        else:
            response['result'] = 'sanitized'

        #return response
        return JsonResponse(response)
