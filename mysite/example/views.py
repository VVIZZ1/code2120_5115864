from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			jsob = json.loads(data)
			#print (jsob)
			#print (type(jsob))
			index = 0
			for i in jsob["demo"]:
				index += 1
			#index = jsob["var"]+str(index)
			return JsonResponse({"log":log})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")

@csrf_exempt
def fib(request):
	jsob = {"startNumber": "0", "length": 10}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			recieved = json.loads(data)
			jsob.update(recieved)

			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])

			loop = range(length)

			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				#print(numarray, fibno, addno)
				fibno = fibno + addno
				print(addno)
				addno = fibno - addno
				print(numarray, fibno, addno)

			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)