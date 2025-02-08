"""
URL configuration for podcast_booking project.

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
from rest_framework.authtoken.views import obtain_auth_token
from appointments.views import UserAppointmentViewSet, AdminAppointmentViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', obtain_auth_token, name='api-token-auth'),
   
    
    path('api/appointments/', UserAppointmentViewSet.as_view({
        'get': 'list', 
        'post': 'create'
    })),
    path('api/appointments/<int:pk>/', UserAppointmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    
    path('api/admin/appointments/', AdminAppointmentViewSet.as_view({
        'get': 'list', 
        'post': 'create'
    })),
    path('api/admin/appointments/<int:pk>/', AdminAppointmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]


