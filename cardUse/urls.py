from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('cardUse', views.CardUsedataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('location', views.cardUseDatatoLoc),
    path('time', views.cardUseDatatoTime)
]
