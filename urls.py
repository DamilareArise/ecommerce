"""
URL configuration for ecommerce project.

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
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import settings
from django.views.generic.base import RedirectView
from ecommerce.productApp.views import home



urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('productApp/', include("ecommerce.productApp.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("ecommerce.userApp.urls")),
    path('cart/', include("ecommerce.cartApp.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# assignment
# Check out the relationship between views, urls, model, forms and templates in Django.