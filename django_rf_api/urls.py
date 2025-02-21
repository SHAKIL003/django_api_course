"""
URL configuration for django_rf_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from api import views
# from drf_api import views
from auth_jwt import views
from rest_framework.routers import DefaultRouter   # used with viewset Class

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
# router.register('studentapi', views.StudentViewSet, basename='student' )  # this one is for simpple Viewset

router.register('studentapi', views.StudentModelViewSet, basename='student' ) # this is for Model Viewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),   # this Url path is for Viewset Class api and Model Viewset
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))

    # path('studentinfo/<int:pk>', views.student_detail),
    # path('studentinfo/', views.student_list),
    # path('studentcreate/', views.student_create),
    # path('studentapi/', views.student_api),

    # path('drfapi/', views.student_api),           # this is function based api views URL
    # path('drfapi/<int:pk>', views.student_api),   # this is function based api views URL

    # path('drfapi/', views.StudentAPI.as_view()),            # this is Class based api views URL
    # path('drfapi/<int:pk>', views.StudentAPI.as_view()),    # this is Class based api views URL

    # path('drfapi/', views.LCStudentAPI.as_view()),            # this is Generic & Mixin Class based api views URL
    # path('drfapi/<int:pk>', views.StudentRetrieve.as_view()),    # this is Generic & Mixin Class based api views URL
    # path('drfapi/', views.StudentCreate.as_view()),
    # path('drfapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('drfapi/<int:pk>', views.RUDStudentAPI.as_view()),

    # path('drfapi/', views.StudentList.as_view()),            # this is Concrete View Class
    # path('drfapi/<int:pk>', views.StudentRetrieve.as_view()),
    # path('drfapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('drfapi/', views.StudentCreate.as_view()),
    # path('drfapi/<int:pk>', views.StudentDestroy.as_view()),
    
    # path('drfapi/', views.StudentListCreate.as_view()),            # this is Concrete View Class,Merged List & Create
    # path('drfapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),




]
