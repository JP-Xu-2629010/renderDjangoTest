"""
URL configuration for myServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from tree01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("vxml/", views.vxml),
    path("viewdb/",views.viewdb, name="viewdb"),
    path("test/", views.test),
    path("case/<int:case_id>/", views.caseCheck),
    path("checkUpload/",views.checkUpload, name = "checkUpload"),
    path("create088/", views.create088),
    path("vxmlUpload/", views.vxmlUpload),
]
