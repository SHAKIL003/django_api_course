from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
# @api_view()
# def home(request):
#     return Response({'res':'This is HOME!'})

# @api_view(['GET'])
# def home(request):
#     return Response({'res':'This is HOME!'})

# @api_view(['POST'])
# def home(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'res':'This is POST Data!'})

# @api_view(['GET','POST'])
# def home(request):
#     if request.method == 'GET':
#         return Response({'res':'This is GET Request!'})

#     if request.method == 'POST':
#         print(request.data)
#         return Response({'res':'This is POST Data!'})

### These are Class Based API Views ###

class StudentAPI(APIView):
    def get(self,request, pk= None,formate = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self,request, formate = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk= None,formate = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated Successfully' })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request, pk= None,formate = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated Successfully' })
        return Response(serializer.errors)
    
    def delete(self,request, pk= None,formate = None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted Successfully' })

### These are Functions based API Views ###

# @api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE' ])
# def student_api(request, pk = None):
#     if request.method == 'GET':
#         # id = request.data.get('id') # this is for getting id from myapp.py
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST' :
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created Successfully'}, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PUT':
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated Successfully' })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':  
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated Successfully' })
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE' :
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted' })


