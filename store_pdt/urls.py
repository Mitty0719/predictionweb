from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('store_pdt', views.StorePdtViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter', views.storePdtById),
    path('update', views.updatePdt),
    path('delete', views.deletePdt)
]
