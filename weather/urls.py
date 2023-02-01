"""weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from rest_framework import routers
from wapi import views

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(
        title="Weather API"
)

router = routers.DefaultRouter()
router.register(r'weather', views.WeatherViewSet, basename='weather')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('api/', include(router.urls)),
    path('api/weather/stats', views.WeatherStatsViewset.as_view({'get': 'list'}))
]
