from django.shortcuts import render
from .models import StorePdt
from store.models import Store
from rest_framework import viewsets
from store_pdt.serializers import StorePdtSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import HttpResponse
from django.core import serializers
from datetime import datetime

# Create your views here.
class StorePdtViewSet(viewsets.ModelViewSet):
    queryset = StorePdt.objects.all()
    serializer_class = StorePdtSerializer #순차화
    
@csrf_exempt
def storePdtById(data):
    loginData = json.load(data)
    
    store = Store.objects.get(store_id = loginData['id'])
    
    pdtList = StorePdt.objects.filter(store_seq = store.store_seq)
    
    pdtList_json = serializers.serialize('json', pdtList)
    
    return HttpResponse(pdtList_json, content_type='application/json')
    
@csrf_exempt
def updatePdt(data):
    updateData = json.load(data)
    seq = updateData['num']
    name = updateData['name']
    disc = updateData['disc']
    price = updateData['price']
    cnt = updateData['cnt']
    id = updateData['id']
    
    print(name, price)
    
    store = Store.objects.get(store_id = id)
    
    if seq is not None:
        update_pdt = StorePdt(
                pdt_seq = seq,
                pdt_name = name,
                pdt_disc = disc,
                pdt_cnt = cnt,
                pdt_price = price,
                regdate = datetime.today(),
                store_seq = store,
            )
    else:
        update_pdt = StorePdt(
                pdt_name = name,
                pdt_disc = disc,
                pdt_cnt = cnt,
                pdt_price = price,
                regdate = datetime.today(),
                store_seq = store,
            )
    update_pdt.save()
    
    return HttpResponse()

@csrf_exempt
def deletePdt(data):
    deleteData = json.load(data)
    seq = deleteData['num']
    delete_pdt = StorePdt.objects.get(pdt_seq = seq).delete()
    delete_pdt.save()
    
    return HttpResponse()