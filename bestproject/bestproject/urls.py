"""bestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from bestapp import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage),
    path('saveapplication/', views.applicationForm),
    path('application/', TemplateView.as_view(template_name = "application.html")),
    path('login/', TemplateView.as_view(template_name = "loginpage.html")),
    path('logincheck/',views.loginCheck),
    path('logout/', views.logout),
    # path('profile/',views.Profile),
    path('home2/',views.home2),
    path('change/',views.changepassword),
    path('pie/',views.chart)
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
