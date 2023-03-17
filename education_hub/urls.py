"""education_hub URL Configuration

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
from django.urls import path
from signup.views import signupaction
from login.views import loginaction
from index.views import indexaction
from contact.views import contactaction
from maths11.views import maths11action
from maths12.views import maths12action
from physics11.views import physics11action
from physics12.views import physics12action
from chemistry11.views import chemistry11action
from chemistry12.views import chemistry12action





urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',signupaction),
    path('',loginaction),
    path('index/',indexaction),
    path('contact/',contactaction),
    path('maths11/',maths11action),
    path('maths12/',maths12action),
    path('physics11/',physics11action),
    path('physics12/',physics12action),
    path('chemistry11/',chemistry11action),
    path('chemistry12/',chemistry12action)
]
