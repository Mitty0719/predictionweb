from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('pdt_keyword', views.WordListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter', views.wordListFilter),
    path('recommend', views.recommendItem),
]
