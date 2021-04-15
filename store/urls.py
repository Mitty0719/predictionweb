from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('stores', views.StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('insert', views.storeInsert),
    path('check', views.storeCheck),
    path('get', views.storeById),
    path('update', views.storeUpdate),
    path('delete', views.storeDelete),
]
