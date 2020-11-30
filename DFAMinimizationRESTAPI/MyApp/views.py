from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
from .MinimizeDFA import serverGateway

# Create your views here.

def _convertResponseToDict(initial,final):
    responseDict = {
        "error":"",
        "initialGraph":str(initial),
        "finalGraph":str(final)
    }
    return responseDict

def _generateErrorResponse(e):
    errorResponse = {
        "error": e.args[0],
        "initialGraph":"",
        "finalGraph":'',

    }
    return errorResponse

@api_view(["POST"])
def MinimizedDfa(request):
    try:
        req = json.loads(request.body)
        alphabets= req['alphabets']
        states = req['states']
        initialState = req['initialState']
        finalStates = req['finalStates']
        transitionList = req['transitionList']
        initialGraphEncodedString,finalGraphEncodedString = serverGateway(alphabets,states,initialState,finalStates,transitionList)

        responseDict = _convertResponseToDict(initialGraphEncodedString,finalGraphEncodedString)
        return JsonResponse(responseDict,safe=True)
    except IndexError as e:
        return JsonResponse(_generateErrorResponse(e),safe=True)
    except ValueError as e:
        return JsonResponse(_generateErrorResponse(e),safe=True)