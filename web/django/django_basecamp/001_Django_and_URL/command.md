# Goals
1. Django가 무엇인지 살펴봅니다.
2. Django의 환경을 구축하고 URL 구조에 대해 익힙니다.

# Django
- Django(장고)는 파이썬으로 작성된 오픈 소스 웹 프레임워크
- 나중에 Django 3~4년차가 되거나 필요에 따라 Django를 더 깊게 공부하고 싶다면 [Django](https://github.com/django/django) 깃허브를 참고하세요.
- 한국 컨트리뷰터도 꽤 됩니다. 여러분도 Django 개발에 기여할 수 있어요.
- 1.x ~ 2.x => 킥스타터 같은 크라우드 펀딩으로 Django를 고도화 해나가기도 했습니다.
- Django 5.x => 성숙단계입니다. 
    - 처음 Django 목표가 현재에 어긋나는 경우를 태생적인 문제로 보고 있는데 내부적으로 아키텍처를 바꾸기 보다는 서드파티 라이브러리를 통해 해결하고 있습니다.
- 오픈소스이기 때문에 보안 취약점이 나오면 공유가 되고, 이것을 다음 버전에서 업데이트 합니다.

# Framework & Library, Third-party
- Framework: 코드의 주권이 나에게 있지 않고 설계도면대로 내 코드를 부품처럼 사용하는 것 (아키텍처가 이미 설계되어 있음)
  - FastAPI, Flask, Django...
- Library: 코드의 주권이 나에게 있고 내가 코드를 호출해서 사용하는 것
  - request, BeautifulSoup, Numpy, Pandas, xlsxwirter...
- Third-party: 예를 들어 Django 서드파티라고 하면 Django와 호환되는 여러 라이브러리 + 프레임웤
- Django 라이브러리 생태계가 활발한 것이 Django의 가장 큰 장점

# Select Django development flow
- ChatGPT로 Django 개발하면 대부분 Monolithic 코드를 뱉어냅니다.
- Monolithic
    - 1개의 서버에서 Django + HTML, CSS, JS
    - 2 ~ 3명 소규모 개발팀에 유리합니다. 서비스를 빠르게 런칭할 수 있어요. 다만 분업에는 최적화되어 있지 않습니다.
    - 자사 서비스인 스터디인은 8개월 정도 모놀리식으로 개발했었습니다. Front-end 개발자가 FE 소스코드를 짜면 백엔드 개발자가 그것을 해체해서 Django 서버에 올리는 작업을 했습니다.
- Microservice
    - 2개의 서버
        - BE 서버: Django
        - FE 서버: HTML, CSS, JS(바닐라js, React, nextjs)
    - 팀 단위가 5명 정도만 되어도 마이크로식은 거의 필수입니다.
    - 팀이 커지면서 스터디인 서비스를 마이크로식으로 새로 개발했습니다. 2년 3개월 정도 개발했어요.

# Features of Django
- ORM(Object-Relational Mapping) 기법: 나는 Python만 할 줄 아는데 이걸로 DB까지 전부 조작하고 싶다? => 실제로 SQL Query를 몰라도 웬만한 서비스는 만들 수 있습니다.
    - 백엔드 개발자는 SQL Query를 반드시 공부하셔야 합니다. 이 Django가 주는 편안함에 안주하시지 않으셨으면 좋겠습니다.
    - DB쿼리를 직접 만져야 하는 일이 반드시 생깁니다.
- 서비스 구현에 대부분의 기능이 구현되어 있으며 Admin 페이지까지 기본적으로 구현이 되어 있는 full-stack 개발 framework입니다.
- 보안: 취약점 테스트를 통해 안정성이 검증된 보안 기능을 제공합니다.
- MTV(Model-Template-View) 패턴: 기능들을 분리하여 개발할 수 있습니다.
    1. Model: 데이터베이스와 상호작용을 하는 컴포넌트
    2. Template: 사용자에게 보여지는 HTML, CSS, JS 등
    3. View: HTTP 요청 처리 및 Model과 Template 연결

# Comparison of Django with other frameworks
- Wordpress Vs Django: 개발 단가가 100배 정도 차이 납니다. 그만큼 난이도 자체가 다릅니다. 해야 하는 과업도 다릅니다. 그렇지만 기본적인 CRUD와 같은 게시판 같은 형태의 서비스라면 Wordpress가 월등히 효율이 좋죠.
- Node Express Vs Django: Django는 다 해줍니다. Node Express는 일일이 개발해야 합니다. 예를 들어 Django 설치만 해도 Admin page가 나옵니다. Node Express는 개발해야 합니다.
- Spring Vs Django: Spring은 세팅하는데 Django 개발이 완료되어 나온다는 농담이 있습니다. 그만큼 개발 속도차이가 많이 납니다.
- 백엔드 개발자의 숙명입니다. 모든 프레임웤들을 조금씩은 다 하게 되실겁니다. 저희 회사만 보더라도 Node 5개, Django 3 ~ 4개 됩니다. 사원 > 대리 > 과장 > 차장 > 팀장 > 부장, 여러분이 팀장급이 되어서 하나의 언어, 하나의 프레임웤, 하나의 분야만 할 수 있을까요?

# django 설계 철학
- https://docs.djangoproject.com/ko/5.0/misc/design-philosophies/
1. Loose coupling (느슨한 결합)
Django 스택의 근본적인 목표는 느슨한 결합, 탄탄한 응집입니다. 프레임워크의 각 계층은 정말로 필요하기 전에는 서로 “알지 못해야” 합니다.

예를 들어, 템플릿 시스템은 웹 요청에 대해 아무 것도 모르고, DB 계층은 데이터 표시에 대해 아무 것도 모르고, View 시스템은 프로그래머가 사용하는 템플릿 시스템을 사용하는지와 무관합니다.

Django는 편의성을 위해 풀 스택으로 제공되지만, 스택의 각 부분은 가능한 한 독립성을 띱니다.

2. Less code (적은 코드)
Django는 가능한 한 최소한의 코드를 사용하며, 틀에 박힌 코드를 배제합니다. Django는 인트로스펙션과 같은 Python의 동적인 기능을 최대한 활용합니다.

3. Quick development (신속한 개발)
21세기 웹 프레임워크의 핵심은 웹 개발의 지루한 부분을 빠르게 만드는 것입니다. Django는 놀랄만큼 빠른 웹 개발을 가능하게 합니다.

4. Don't repeat yourself (DRY)
고유한 개념 및 데이터는 단 한 번, 단 한 곳에 존재하는 것으로 족합니다. 중복성은 나쁜 것이고, 정규화는 좋은 것입니다.

그러한 이유로, 본 프레임워크는 최소한의 것들을 가지고 최대한의 것을 만들어내도록 합니다.

# Django 관련 VSC 익스텐션

- black formatter: 권고사항에 맞지 않는 문법들을 강제로 권고사항에 맞춰줍니다. 협업할 때 주로 사용하게 됩니다.
- django: 자동완성, ChatGPT와 코파일럿이 나오면서 자동완성에 대한 중요성이 많이 낮아졌습니다.
- Thunder Client: http request, response test 도구입니다. postman 같은 것을 예전에는 많이 사용했으나 요즘에는 VSC 익스텐션들이 워낙 잘 되어 있어서 서비스 만드는데 큰 도움이 됩니다.


# django
```bash
# 터미널을 열어 작업
#     - 터미널(Ctrl + `), 단축키 대신 VSC에서 Terminal > new Terminal
# 이 명령어는 powershell 에서 치고 있습니다.
# 터미널 오른쪽 상단 +버튼 옆 아래 꺾쇠 버튼 눌러스 powershell을 열어주세요.

python --version
# 파이썬 버전 확인
mkdir mysite
# mysite라는 폴더 생성 => 마우스 클릭하셔서 생성하는 것과 차이 없습니다. 보통 mysite라는 이름 대신 프로젝트 이름을 넣습니다.
cd mysite
# 폴더 이동
python -m venv venv
# 가상 환경 설정
#     - 가상환경은 선택이 아니라 필수 입니다.
#     - 가상환경을 왜 잡을까요? 관리, 이관, 업데이트 등에 중요한 거점이 됩니다.
#     - pip list를 쳐보세요. 많은 python 라이브러리가 보이죠? 여기서 소숫점 3번째 짜리까지 안맞으면 작동 안되는 경우도 허다합니다. => 가상 환경은 통째로 다 이동합니다.
#     - python -m venv [name of virtual environment]

# 가상환경속으로 들어가기
source venv/bin/activate # mac, linux

# which python을 통해서 가상환경에 있는 python을 사용하는지 확인할 수 있다.

pip install django
# django를 최신 버전으로 설치합니다. 구버전 설치 하고 싶으시면 pip install django==4.0

django-admin startproject tutorialdjango .
# 띄고 점 꼭 하셔야 합니다!!!! 설치된 django로 초기세팅 하겠다라는 명령어 입니다. 암기하는 명령어 입니다. tutorialdjango는 이름입니다. 여러분 마음대로 지셔도 되는 이름입니다.

python manage.py migrate
# 이 명령어는 우리가 짠 python 코드를 DB에 반영하는 코드입니다. 다만! 실무에서는 이 migrate라는 명령어를 초기 세팅이 다~~~ 끝나고 합니다. 특히 User나 Admin 가입 소스코드를 만지면 먼저 migrate를 하면 error가 나는 경우가 있습니다. 처음에 migrate를 하면 기본적으로 django에서 세팅해주는 소스코드를 DB에 생성, 반영합니다.

python manage.py runserver
# 파이썬 서버를 구동합니다. 이 명령어가 실행되는 동안에만 서버가 실행됩니다. Ctrl 누르고 서버 URL을 클릭해보세요.


################################
# tutorialdjango/settings.py

ALLOWED_HOSTS = ["*"] # 웹 서비스에 접속할 수 있는 사람을 모든사람으로 설정

################################

# URL에 따라 보통 1개의 앱을 만듭니다. 이름만 앱입니다. 실제로 다른 애플리케이션이라는 얘기가 아닙니다. 이유는 권한, 그 안에 들어가는 로직 등을 별도로 관리하기 위해서 입니다. 예를 들어 회원 게시판이 있고 자유 게시판이 있다면 회원 게시판에는 회원만 글을 써야 합니다. 이런 식으로 URL에 따른 권한과 로직을 별도로 관리하기 위해서 앱을 만들어 관리합니다. 
# 앱 = 폴더이자 기능, 모듈이라고 생각하면 쉽다.

# https://www.studyin.co.kr/ => A
# https://www.studyin.co.kr/offline => B
# https://www.studyin.co.kr/online => C

################################

# Terminal에서 Ctrl + C 눌러서 서버를 종료시켜 주세요! => 우리 서비스는 작동되지 않습니다!
# 아래 명령어는 main이라는 앱을 하나 만들겠다는 것입니다. 기획이 되어 있는 상태에서는 이 명령어를 수십번 쳐서 세팅하고 들어갑니다.
python manage.py startapp main

################################
# tutorialdjango/settings.py

```

```python
# 앱을 만들면 settings.py에 해당 앱을 등록해야 합니다.
INSTALLED_APPS = [
    "main", # 보통은 마지막에 넣는데 맨 위에 넣으시는 분도 있으십니다.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

################################
# URL 구조 작성(기획 단계), 문서입니다. 
# 다른 곳에 작성하는 것이 아닙니다.

# 기획
# www.seunan.com/admin admin 페이지
# www.seunan.com/      메인페이지
# www.seunan.com/a     a페이지
# www.seunan.com/b     b페이지
# www.seunan.com/c     c페이지
# www.seunan.com/seunan 이호준 소개 페이지
# www.seunan.com/orm   오름 소개 페이지

################################

# URL 설계한 것을 반영하는 곳!
# tutorialdjango/urls.py에 반영!
# 실제 실무에서는 앱별로 분리하여 관리합니다!

from django.contrib import admin
from django.urls import path
from main.views import index, a, b, c, seunan, orm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("a/", a),
    path("b/", b),
    path("c/", c),
    path("seunan/", seunan),
    path("orm/", orm),
]

################################
# 설계한 URL에 접속했을 때 실제 보게될 텍스트는 views.py에서!
# HttpResponse는 주로 테스트 용도로 사용합니다.
# main > views.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>메인화면 입니다!</h1>")


def a(request):
    return HttpResponse("<h1>a 입니다!</h1>")


def b(request):
    return HttpResponse("<h1>b 입니다!</h1>")


def c(request):
    return HttpResponse("<h1>c 입니다!</h1>")


def seunan(request):
    return HttpResponse("<h1>seunan 입니다!</h1>")


def orm(request):
    return HttpResponse("<h1>orm 입니다!</h1>")


################################

python manage.py runserver

# 모든 페이지 정상작동 확인 + 이상한 URL 입력시 애러 확인
# settings.py에 DEBUG도 False로 해봐서 출력되는 화면도 확인

################################
# 실무에서 사용하는 형태(FBV)로 views.py 수정!

from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def a(request):
    return render(request, "main/a.html")


def b(request):
    return render(request, "main/b.html")


def c(request):
    return render(request, "main/c.html")


def seunan(request):
    return render(request, "main/seunan.html")


def orm(request):
    return render(request, "main/orm.html")


################################

mysite > main > templates > main > index.html
mysite > main > templates > main > a.html
mysite > main > templates > main > b.html

# 위에 3개만 생성을 했습니다.
mysite > main > templates > main > c.html
mysite > main > templates > main > seunan.html
mysite > main > templates > main > orm.html

################################

각 html 안에는 구분이 가능한 텍스트를 넣어주세요.
1, 2, 3 등에 텍스트면 됩니다.

################################

Ctrl + C 한 다음 다시
python manage.py runserver

################################

TemplateDoesNotExist at /c/
위와 같은 error는 어떠한 경우에 나오는지 숙지해주세요.

################################
```
