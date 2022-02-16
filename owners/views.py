from unicodedata import name
from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)  
            owner = Owner.objects.create(    
                name  = data['name'],        
                email = data['email'],
                age   = data['age']
            ) 
        # request.body는 front에서 준 정보
        # json.lods는 그 정보를 딕셔너리 형태로 바꾸는것
        # 그걸 data 라는 변수에 담는다 data에는 딕셔너리가 담긴다.
        # 프론트에서 준거 저장하는 과정임 
        # crud1때 했던 create하는 과정
        
            return JsonResponse({"message": "owner created"}, status=201)
        except KeyError:
            return JsonResponse({"message": "KeyError"}, status=400)
                                    
        #키 에러가 날수도 있으니깐 에러처리를 해줘야 한다 (try-except문 사용해서)
       

class Dogview(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            owner = Owner.objects.get(name=data['owner'])
            Dog.objects.create(
                name  = data['name'],
                age   = data['age'],
                owner = owner
            )
            return JsonResponse({"message": "SUCCESS"},  status=201)
        except KeyError:
            return JsonResponse({"message": "KeyError"}, staus=400)
