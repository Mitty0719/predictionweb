'''
Created on 26 Mar 2021

@author: sprou
'''
from rest_framework import serializers
from .models import CardUsedata

class CardUsedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardUsedata #모델 설정
        fields = '__all__'
        #fields = ('num', 'id', 'password', 'name', 'category', 'location', 'regdate') #필드 설정
