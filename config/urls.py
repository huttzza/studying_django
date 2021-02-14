"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

#from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pybo/', views.index), #pybo/ 슬래쉬 없이 주소 입력해도 장고가 자동으로 슬래쉬를 붙여준다
    # pybo/ URL과 pybo/views.py의 함수 index와 연결해주는 것!
    path('pybo/', include('pybo.urls')), #pybo/urls.py 의 url 매핑을 참조하라는 뜻
]
