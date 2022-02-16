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

    # def get(self, request):
    #     result = []            # owner 정보를 담을 빈 리스트 선언
    #     owners = Owner.objects.all()   # all()메소드 이용해서 Owner의 모든 정보 쿼리셋으로 불러와서 owners에 저장

    #     for owner in owners:     # for문 이용해서 owners에 저장된 쿼리셋 하나씩 가져와서 owner에 저장
    #         owner_information = {
    #             'name'  : owner.name,
    #             'email' : owner.email,
    #             'age'   : owner.age
    #         }
    #         # owner 불러올때마다 딕셔너리 형태로 name, email, age 값 가져와서 result에 append하기
    #         result.append(owner_information)
    #     # 최종적으로 [{},{},{}...,{}] 로 담긴다. 
    #     return JsonResponse({'result':result}, status=200)


    # get 강아지리스트 (이름, 나이, 주인이름 포함) - dog가 owner를 정참조 하는 상황에서 owner에서 dog역참조(_set 이용해서) 해서 get요청하기
    def get(self, reuqest):
        result = []
        owners = Owner.objects.all()

        for owner in owners:
            dogs     = owner.dog_set.all() # owner 에는 dog 정보가 없다 그런데 dog는 owner가 foreign 키로 물려있어서 owner에서 dog 정보 가져오려면 dog_set으로 owner를 물고있는 dog 정보 가져올수 있다. 
            dog_list = []
                # 역참조 하고 싶을 때는 역참조 하고 싶은 클래스를 소문자로 적고 _set 하면된다. 
                # 그거 아니면 첨부터 models.py작성시에 역참조 하고싶은 부분에 옵션으로 related_name= 붙여준다.
            for dog in dogs:
                dog_information = {
                    'name' : dog.name,
                    'age'  : dog.age
                }
                dog_list.append(dog_information)

            owner_information = {
                'name'  : owner.name,
                'email' : owner.email,
                'age'   : owner.age,
                'dogs'  : dog_list
            }
            result.append(owner_information)
        return JsonResponse({'result': result}, status=200)




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

    def get(self, request):
        result = []
        dogs = Dog.objects.all()

        for dog in dogs:
            dog_information = {
                'name'  : dog.name,
                'age'   : dog.age,
                'owner' : dog.owner.name
            }
            result.append(dog_information)
        return JsonResponse({'result':result}, status=200)
