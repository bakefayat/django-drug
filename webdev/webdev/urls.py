"""webdev URL Configuration

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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from account.views import Login
from account.views import Register, activate
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('register/pending/', TemplateView.as_view(template_name='registration/register_done.html') ,name='register-pending'),
    path('register/complete/', TemplateView.as_view(template_name='registration/register_complete.html') ,name='register-complete'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('account/', include('account.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
