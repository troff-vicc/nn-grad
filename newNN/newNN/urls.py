"""
URL configuration for newNN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index),
    path('place', views.place),
    path('child', views.child),
    path('hotel', views.hotel),
    path('help', views.help),
    path('place/<int:id>', views.placeOne),
    path('hotel/<int:id>', views.hotelOne),
    path('place/edit/<int:id>', views.placeEdit),
    path('add', views.add),
    path('admin', views.admin),
    path('log', views.log),
    path('action', views.action)
    
]
