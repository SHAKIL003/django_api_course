from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view()
# def home(request):
#     return Response({'res':'This is HOME!'})

# @api_view(['GET'])
# def home(request):
#     return Response({'res':'This is HOME!'})

@api_view(['POST'])
def home(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'res':'This is POST Data!'})


