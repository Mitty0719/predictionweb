'''
Created on 4 Apr 2021

@author: sprou
'''
from rest_framework import serializers
from .models import WordList

class WordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordList #모델 설정
        fields = '__all__'
        #fields = ('num', 'id', 'password', 'name', 'category', 'location', 'regdate') #필드 설정
