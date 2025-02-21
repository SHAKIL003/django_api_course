### Model ViewSets
## And Below are Model Viewsets , too simple to implement, its url and Viewsets url are same only class name should be sepecified.

# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import viewsets

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

### there is also another viewset called ReadOnlyModelViewSet, through which only data can viewed.

### ViewSets
## Below are code for Viewsets for each CRUD Operations
# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework import viewsets

# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         print("**********List**********")
#         print("Basename:", self.basename)
#         print("Action:", self.action)
#         print("Detail:", self.detail)
#         print("Suffix:", self.suffix)
#         print("Name:", self.name)
#         print("Description:", self.description)
#         stu = Student. objects. all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.
#             HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.
#         HTTP_400_BAD_REQUEST)
#     def update(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.
#         HTTP_400_BAD_REQUEST)
#     def partial_update(self,request, pk):
#         id =pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data,
#         partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)
#     def destroy(self,request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})

### This is now more updated Views , called Concrete Views which extends from GenericAPIView and Mixins
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentListCreate(ListCreateAPIView):   # Merged Two Views
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):   # Merged Three Views
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

### GenericAPIView and Model Mixin
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# ### As we have created individual classess and its realted URL,
# ### so to minimize its URLs we can also Group these classes on the bases of pk,

# ### List and Create -- Pk not Required , will be grouped together
# class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin) :
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, ** kwargs):
#         return self.list(request, *args, ** kwargs)
#     def post(self, request, *args, ** kwargs):
#         return self.create(request, *args, ** kwargs)
    
# # class StudentCreate(GenericAPIView, CreateModelMixin) :  # this is merged with the above one
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer
# #     def post(self, request, *args, ** kwargs):
# #         return self.create(request, *args, ** kwargs)

# ### Retrieve - Update - Destroy --- Pk Required,  so merged with each other
# class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin) :
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, ** kwargs):
#         return self.retrieve(request, *args, ** kwargs)
    
#     def put(self, request, *args, ** kwargs):
#         return self.update(request, *args, ** kwargs)

#     def delete(self, request, *args, ** kwargs):
#         return self.destroy(request, *args, ** kwargs)

# from django.shortcuts import render
# from rest_framework.response import Response
# # from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status

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

# class StudentAPI(APIView):
#     def get(self,request, pk= None,formate = None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
    
#     def post(self,request, formate = None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created Successfully'}, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request, pk= None,formate = None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated Successfully' })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self,request, pk= None,formate = None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated Successfully' })
#         return Response(serializer.errors)
    
#     def delete(self,request, pk= None,formate = None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted Successfully' })

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


