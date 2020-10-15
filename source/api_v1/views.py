from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only Get request')

def math(request, *args, **kwargs):
    answer = {}
    summ = ''
    try:
        data = json.loads(request.body)
        a = int(data['A'])
        b = int(data['B'])
        if request.path == "/add/":
            summ = a + b
        elif request.path =="/subtract/":
            summ = a + b
        elif request.path == "/multiply/":
            summ = a * b
        elif request.path == "/divide/":
            summ = a / b
        else:
            summ = None
        answer['result'] = summ
        print(answer)
        return JsonResponse(answer)
    except Exception as e:
        response = JsonResponse({"error": str(e)})
        response.status_code = 400
        return response





#
# def subtract(request, *args, **kwargs):
#     answer = {}
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         summ= data['A'] - data['B']
#         answer['summ'] = summ
#     return JsonResponse(answer)
#
#
# def multiply(request, *args, **kwargs):
#     answer = {}
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         summ= data['A'] * data['B']
#         answer['summ'] = summ
#     return JsonResponse(answer)
#
#
# def divide(request, *args, **kwargs):
#     answer = {}
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         summ= data['A'] / data['B']
#         answer['summ'] = summ
#     return JsonResponse(answer)