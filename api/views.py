import io
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# Model Object - Single Student Data

def student_detail(request, pk):
    stu = Student.objects.get(id= pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type ='application/json')
    return JsonResponse(serializer.data)

# Query List - All Students Data
def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu, many = True)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type ='application/json')
    return JsonResponse(serializer.data, safe=False)

# Creating/Inserting Data View
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Data Inserted Successfully'}
            json_data2 = JSONRenderer().render(msg)
            return HttpResponse(json_data2, content_type = 'application/json')
        json_data2 = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data2, content_type = 'application/json')

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data3 = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data3, content_type = 'application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data3 = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data3, content_type = 'application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Inserted Successfully'}, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        # to full update all data need to passed and [partial =  True] should be removed form parameters
        serializer = StudentSerializer(stu, data = pythondata, partial = True)  # this is for partial update
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Updated Successfully'}, status = 201)
        return JsonResponse(serializer.errors, status = 400)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return JsonResponse({'msg': 'Data Deleted Successfully'}, status = 201)
        