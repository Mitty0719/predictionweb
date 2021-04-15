from django.shortcuts import render
from rest_framework import viewsets
from .models import WordList
from .serializers import WordListSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import HttpResponse
from django.core import serializers
from store.models import Store
from datetime import datetime
from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
import urllib
import xmltodict
from numpy import unicode
import chardet

# Create your views here.
class WordListViewSet(viewsets.ModelViewSet):
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer #순차화

@csrf_exempt
def wordListFilter(data):
    data = json.load(data)
    s_keyword = data['keyword']
    year = data['year']
    mon = data['mon']
    
    query = WordList.objects.filter(keyword=s_keyword, word_year=year, word_mon=mon)
    
    # query_result = []
    # for que in query:
        # query_result.append({'keyword':que.word_word, 'word_cnt':que.word_cnt})
    
    query_list = serializers.serialize('json', query)
    return HttpResponse(query_list, content_type="application/json; charset=utf-8")


@csrf_exempt
def recommendItem(data):
    jsonData = json.load(data)
    local_id = jsonData['id']
    
    store = Store.objects.get(store_id=local_id)
    category = store.store_ctg
    
    month = datetime.today().month
    
    itemList = WordList.objects.filter(keyword=category, word_mon = month)
    
    reData = {}
    
    for item in itemList:
        word = item.word_word
        if reData.get(item.word_word) is not None:
            reData[word] = reData.get(word) + item.word_cnt
        else:
            reData[word] = item.word_cnt
            
    def sortByVal(x):
        return x[1]
    
    res = sorted(reData.items(), key=sortByVal, reverse=True)
    highData = res[0]
    highKeyword = highData[0]
    
    #가장 높은 빈도의 단어로 상품 리스트 추출
    url = 'http://openapi.11st.co.kr/openapi/OpenApiService.tmall?key=1fc323faf14a0ddc1479e3d6f04069f6&apiCode=ProductSearch&keyword='+urllib.parse.quote_plus(category +" "+ highKeyword)+'&sortCd=G'
    request = Request(url)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('euc-kr')
    
    jsonString = json.dumps(xmltodict.parse(response_body), indent=4, ensure_ascii=False)
    # print(jsonString)
    
    #jsonStr를 Dict객체로 변환
    jsonDict = json.loads(jsonString.replace("'", "\""))
    
    dataResponse = jsonDict['ProductSearchResponse']
    dataProducts = dataResponse['Products']
    dataProduct = dataProducts['Product']
    
    productResult = {}
    getPdtCnt = 10
    
    for i in range(0, getPdtCnt):
        product = dataProduct[i]
        productResult['pdt'+str(i+1)] = {'title': product['ProductName'], 'image': product['ProductImage'], 'page': product['DetailPageUrl'],'price': product['SalePrice']}
    
    # jsonResult = serializers.serialize('json', productResult)
    jsonResult = json.dumps(productResult)
    
    return HttpResponse(jsonResult, content_type="application/json; charset=utf-8")


















