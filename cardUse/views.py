from django.shortcuts import render
from .models import CardUsedata
from .serializers import CardUsedataSerializer
from rest_framework import viewsets
from django.http.response import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from scipy.special._ufuncs import pdtr

# Create your views here.
class CardUsedataViewSet(viewsets.ModelViewSet):
    queryset = CardUsedata.objects.all()
    serializer_class = CardUsedataSerializer #순차화
   
   
   
@csrf_exempt
def cardUseDatatoLoc(data):
    locChartData = json.load(data)
    
    in_year = locChartData['year']
    in_mon = locChartData['mon']
    in_ctg = locChartData['ctg']
    # in_age = locChartData['age']
    print(in_year, in_mon, in_ctg)
    cardUseList = CardUsedata.objects.filter(use_ctg=in_ctg)
    cardUseDict = {}
    
    for card in cardUseList:
        year = card.use_date[0:4]
        month = card.use_date[4:7]
        if year == in_year and month == in_mon:
            if cardUseDict.get(month) is not None:
                cardUseDict[card.use_loc] = cardUseDict.get(card.use_loc) + card.use_pay
            else:
                cardUseDict[card.use_loc] = card.use_pay
    
    cardUseJson = json.dumps(cardUseDict)
    
    return HttpResponse(cardUseJson, content_type='application/json; charset=utf-8')

@csrf_exempt 
def cardUseDatatoTime(data):
    timeChartData = json.load(data)
    
    in_year = timeChartData['year']
    in_ctg = timeChartData['ctg']
    # in_age = timeChartData['age']
    in_loc = timeChartData['loc']
    print(in_year, in_ctg, in_loc)
    
    cardUseList = CardUsedata.objects.filter(use_ctg = in_ctg, use_loc = in_loc) # use_age = in_age,
    
    cardUseDict = {}
    
    for card in cardUseList:
        year = card.use_date[0:4]
        month = card.use_date[4:7]
        if year == in_year:
            if cardUseDict.get(month) is not None:
                cardUseDict[month] = cardUseDict.get(month) + card.use_pay
            else:
                cardUseDict[month] = card.use_pay
    
    cardUseJson = json.dumps(cardUseDict)
    
    return HttpResponse(cardUseJson, content_type="application/json; charset=utf-8")

































