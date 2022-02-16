"""CRUD2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# main ursl.py는 분기를 나누어주는 역할 
# 어느 곳으로 갈건지 경로를 표시해주는 곳

from django.urls import path, include

urlpatterns = [
    path("owners", include("owners.urls")),
]

# http://127.0.0.1:8000/ 이 이후에 오는 url주소가 path의 'owners'라고 생각하면됨 그러니깐 위에 url패턴대로라면
# http://127.0.0.1:8000/owners 라고 httpie 에 적어주어야 한다. owners를!