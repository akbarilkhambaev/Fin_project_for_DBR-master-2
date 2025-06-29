"""
URL configuration for Fin_v2_by project.

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

urlpatterns = [
    # Main app URLs
    path('',include('fin_app_v2.urls')),
    path('', include('fin_app_v2.api_urls')),
    path('', include('fin_app_v2.api_task_urls')),
    path('', include('fin_app_v2.api_tmk_task_urls')),
]
