# app을 처음 생성할때는 없는 파일이다. 
# main urls에서 app urls로 경로 설정해줬으니깐 (path("owners")) app 에서 urls.py 만들어서 
# 메인에서 이쪽으로 경로 설정해줬고 이쪽에선(app urls)어느 로직으로 보내줄지를 정하는 곳!

from django.urls import path
from owners.views import Dogview, OwnerView

urlpatterns = [
    path("", OwnerView.as_view()),
    path("/dogs", Dogview.as_view()) 
]                           
# as_view 가 해주는 역할 중에 하나로 
# owner 클래스 안에 http 메소드랑 똑같은 이름이 있다면 그걸 실행해줌(기능까지)
# 그래서 함수 이름 정의 할때 http 메소드랑 이름똑같이 만드는것임

#path에 빈문자 "" 들어간 이유는
#http://127.0.0.1:8000/owners 뒤에 공백으로 두어야 OwnerView.as_view()를 실행한다는 뜻