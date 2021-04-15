from rest_framework import viewsets
from .serializers import StoreSerializer
from .models import Store
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from datetime import datetime
from django.core import serializers
from django.http.response import HttpResponse


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer #순차화

@csrf_exempt
def storeById(data):
    insertData = json.load(data)
    store = Store.objects.get(store_id=insertData['id']);
    storeStr = {}
    storeStr['id'] = store.store_id
    storeStr['name'] = store.store_name
    storeStr['category'] = store.store_ctg
    storeStr['location'] = store.store_loc
    storeStr['tel'] = store.store_tel
    
    jsonStore = json.dumps(storeStr) #dictionary to json
    
    return HttpResponse(jsonStore, content_type='application/json; charset=utf-8')

@csrf_exempt
def storeInsert(data):
    insertData = json.load(data)
    # print(insertData['id'])
    dto = Store(
            store_id = insertData['id'],
            store_pwd = insertData['password'],
            store_name = insertData['storeName'],
            store_ctg = insertData['category'],
            store_loc = insertData['storeLocation'],
            store_tel = insertData['storeTel'],
            regdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    dto.save()
    return HttpResponse()

@csrf_exempt
def storeCheck(data):
    checkData = json.load(data)
        
    if Store.objects.filter(store_id=checkData['id']).exists():
        store = Store.objects.get(store_id=checkData['id'])
        if store.store_pwd == checkData['password'] : 
            context = "success"
        else :
            context = "passwordError"
    else :
        context = "idError"
    
    return HttpResponse(context)

@csrf_exempt
def storeUpdate(data):
    updateData = json.load(data)
    
    store = Store.objects.get(store_id = updateData['id'])
    
    update_store = Store(
            store_seq = store.store_seq,
            store_id = updateData['id'],
            store_pwd = updateData['password'],
            store_name = updateData['storeName'],
            store_ctg = updateData['category'],
            store_loc = updateData['storeLocation'],
            store_tel = updateData['storeTel'],
            regdate = store.regdate
        )
    update_store.save()
    
    return HttpResponse("success")
    
    

@csrf_exempt
def storeDelete(data):
    deleteData = json.load(data)
    Store.objects.get(store_id = deleteData['id']).delete()
    
    return HttpResponse("success")