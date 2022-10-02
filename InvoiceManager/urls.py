"""InvoiceManager URL Configuration

The `urlpatterns` list routes URLs to views.py. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views.py
    1. Add an import:  from my_app import views.py
    2. Add a URL to urlpatterns:  path('', views.py.home, name='home')
Class-based views.py
    1. Add an import:  from other_app.views.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from InvoiceManager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('healthcheck/', views.say_hello),
    path('addclient/', views.clientmanager),
    path('addinvoice/', views.invoicemanager),
    path('__debug__/', include(debug_toolbar.urls)),
    path('display-pdf/', views.displaypdf, name='display-pdf'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]