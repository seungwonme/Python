# Flask
Flask는 표준을 따르는 **마이크로프레임워크**라고 할 만큼 규모가 작다.

## Dependencies
- Werkzeug: 라우팅, 디버깅, 웹 서버 게이트웨이 인터페이스(WSGI) 등의 핵심 기능을 제공하는 라이브러리
- jinja2: 템플릿 엔진
두 의존성 모두 Flask의 코어 개발자가 개발했다.

## Virtual Environment
가상환경은 개별적으로 설치하는 패키지에 대한 파이썬 인터프리터의 프라이빗 복사본을 만들어준다. 
이를 통해 프로젝트 간의 패키지 충돌을 방지할 수 있다.
```bash
$ python -m venv venv
$ source venv/bin/activate
```

## Installation
```bash
$ pip install Flask
```

## Basic Application Structure

### Initialization
Flask 어플리케이션은 `Application Instance`를 생성해야 한다. \
웹 서버는 클라이언트로부터 수신한 모든 request를 이 오브젝트(Application Instance)에서 처리하는데 \
이 때, 웹 서버 게이트웨이 인터페이스(WSGI)를 사용한다. \
Application Instance는 Flask 클래스의 오브젝트이며 다음과 같이 생성한다.
```python
from flask import Flask # Flask 웹 프레임워크에서 Flask 클래스를 import
app = Flask(__name__) # Flask 클래스의 인스턴스 생성
```
Flask 클래스 생성자에 필요한 한 가지 인수는 `Main Module의 이름`이나 `Application Package의 이름`이다. \
대부분의 애플리케이션에서는 파이썬의 `__name__`을 사용한다.
> __name__은 현재 모듈의 이름을 나타내는 내장 변수이다. \
> 파이썬 스크립트가 독립적으로 실행될 때는 "main"으로 설정되고, 모듈로 import될 때는 모듈의 이름으로 설정된다.

### Routing
웹 브라우저와 같은 클라이언트는 웹 서버에 `Request`를 전송 \
애플리케이션 인스턴스는 각 URL 리퀘스트 실행을 위해 어떤 코드가 필요한지 식별해야 한다. \
식별하기 위해 URL을 함수에 매핑하는 기능이 필요하다. URL과 해당 URL을 처리하는 함수의 관련성을 `Route`라고 한다.

#### Decorator
- Flask 애플리케이션에서 `Route`를 정의하는 가장 손쉬운 방법
- `@app.route()` 데코레이터를 사용하여 URL을 함수에 매핑
```python
@app.route('/') # 루트 URL에 대한 라우트
def index(): # URL을 처리하는 함수(view function)
    return '<h1>Hello, World!</h1>' # 클라이언트에게 반환할 Response
```

#### Dynamic Routes
- Flask는 Dynamic Routes를 route 데코레이터에 있는 특별한 문법을 사용하여 지원한다.
- URL의 일부를 변수로 사용하려면 `<variable_name>`을 사용하여 동적 URL을 정의할 수 있다.
- 뷰 함수가 실행되면 Flask는 동적 컴포넌트를 인수로 전송한다.
```python
@app.route('/user/<name>') # 동적 URL
def user(name):
    return '<h1>Hello, %s!</h1>' % name
```
예제는 문자열이지만 \<converter:variable_name\> 형식을 사용하여 타입에 의한 Route를 지정할 수 있다.
`int`, `float`, `path`를 지원한다.

### Server Startup
애플리케이션 인스턴스는 `run` 메서드를 갖고 있으며 이 메서드를 호출하여 Flask의 통합 개발 웹 서버를 실행할 수 있다.
```python
if __name__ == '__main__': # 스크립트가 직접 실행될 때만 서버를 실행
    app.run(debug=True) # run 메서드의 여러 옵션 인수 사용 가능, debug=True는 디버그 모드(디버거와 리로더를 활성화)
```

### Request and Response
Flask가 클라이언트에서 Request를 수신하면 처리하기 위해 뷰 함수에서 사용 가능한 몇 개의 오브젝트를 생성해야한다. \
좋은 예는 `Request Object`인데 이 오브젝트는 클라이언트에 의해 송신된 HTTP Request를 캡슐화한다. \
이 객체는 요청과 관련된 데이터, 예를 들어 요청 메소드, 폼 데이터, 쿠키, 헤더 등에 대한 정보에 접근할 수 있게 해준다. \
\
Multi-Thread Server를 고려한다면, 각 Request는 별도의 Thread에서 처리되므로 Request Object는 전역 변수가 될 수 없다.
\
Flask 애플리케이션 내에서 Request Object에 접근하는 방법은 다음과 같다:
1. **Contexts를 사용하여 글로벌하게 접근**: Flask는 Request-Response 사이클을 처리하는 동안 특정 객체들을 글로벌하게 접근할 수 있게 하는 컨텍스트를 제공한다. Request Object는 Request Contexts의 일부로, Request이 활성화되어 있는 동안 전역에서 접근할 수 있다. Contexts를 사용하면 Flask는 다른 스레드의 개입없이 임의의 변수들이 전역적으로 스레드에 안전하게 접근할 수 있게 해준다. **Flask에서 Request Object에 접근하는 표준적인 방법**
2. *Request Object를 뷰 함수의 인수로 직접 전달*: 모든 뷰 함수의 인수에 일일히 집어 넣어야 하므로 이 방법은 Flask에서 일반적으로 사용되지 않음
```python
from flask import request # request object를 import

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent') # request object의 headers 속성을 사용하여 User-Agent 헤더를 가져옴
    return '<p>Your browser is %s</p>' % user_agent
```

#### Context
| Variable Name | Context | Description |
| --- | --- | --- |
| current_app | Application Context | 현재 활성화된 Application을 위한 Application Instance |
| g | Application Context | Request를 처리하는 동안 Application이 임시 스토리지를 사용할 수 있게 해주는 객체 |
| request | Request Context | 클라이언트로부터 수신한 HTTP Request의 콘텐츠를 캡슐화하는 Request Object |
| session | User Session Context | 클라이언트 세션을 위한 Session Object |

#### Request Dispatching
애플리케이션의 클라이언트에서 Request를 수신하면, 그 것을 서비스하기 위해 실행할 뷰 함수를 검색해야 한다.\
Flask는 애플리케이션 `URL 맵`에서 리퀘스트에 주어진 URL을 검색한다.\
URL 맵은 URL과 뷰 함수 사이의 매핑을 저장하는 데이터 구조이며 다음과 같이 생성된다.
1. `@app.route()` 데코레이터를 사용하여 뷰 함수에 URL을 매핑
2. `add_url_rule()` 메서드를 사용하여 뷰 함수에 URL을 매핑

#### Request Hooks
Flask는 Request 처리하기 전과 후에 실행할 수 있는 `Hooks`를 제공한다.
| Hook | Description |
| --- | --- |
| before_first_request | 첫 번째 Request가 처리되기 전에 실행 |
| before_request | 각 Request 전에 실행하는 함수 등록 |
| after_request | 처리되지 않은 예외가 발생하지 않는다면, 각 Request 후에 실행하는 함수 등록 |
| teardown_request | 처리되지 않은 예외가 발생하더라도, 각 Request 후에 실행하는 함수 등록 |

#### Response
뷰 함수의 응답으로는 Response로 값뿐만 아니라 `상태 코드`, 헤더 등을 포함할 수 있으며, 값을 튜플로 반환하는 대신 `Response Object`를 반환할 수 있다.
```python
from flask import make_response

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
```

##### Redirects
- Page를 포함하지 않으며 새로운 Page를 로드하는 URL을 브라우저에 전달
- 302 상태 코드와 Location 헤더에 있는 리다이렉트할 UR을 사용하여 알려줌
```python
from flask import redirect

@app.route('/')
def index():
    return redirect('https://www.google.com')
```

##### Abort
- 에러 핸들링을 위해 사용
- 특정 상태 코드와 메시지를 반환
```python
from flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name
```

### Extensions
Flask는 확장을 통해 기능을 확장할 수 있다. 

## Templates
### Logic
뷰 함수의 확실한 Tasksms Request에 대해 Response를 반환하는 것이다. \
\
사용자가 웹 사이트에 새로운 계정을 생성한다면
1. 사용자가 웹 폼에 이메일 주소와 패스워드를 입력하고 제출
2. 서버는 사용자로부터 받은 데이터를 포함하는 Request를 수신
   - Flask는 이 Request를 처리하는 뷰 함수에 Request를 Dispatch
   - 뷰 함수는 DB에 연결하여 새로운 사용자를 생성하고 응답을 브라우저로 반환
이 두 가지의 Task는 각각 `Business Logic`과 `Presentation Logic`이라고 한다. \
이 Logic을 Template에 넣으면 유지보수가 쉬워지기 때문에 Flask는 Jinja2 템플릿 엔진을 사용한다.

### Jinja2
#### render_template()
- Flask는 루트 폴더 안에 `templates` 폴더를 찾아 템플릿을 찾는다.
- Flask에서 제공되는 `render_template()` 함수는 애플리케이션과 Jinja2 템플릿 엔진을 연결한다.
- 첫 번째 인수는 템플릿 파일의 이름이며, 나머지 인수는 템플릿에 전달할 변수들의 Key-Value 쌍이다.
```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html 파일을 렌더링

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) # templates/user.html 파일을 렌더링하고 name 변수를 전달
```

#### Variables
- Jinja2는 템플릿에 변수를 삽입하는 데 사용할 수 있는 `{{ variable }}` 구문을 제공한다.
- `render_template()` 함수의 두 번째 인수로 전달된 변수는 템플릿에서 사용할 수 있다.
```html
<p>A value from a dictionary: {{ mydict['key'] }}</p>
<p>A value from a list: {{ mylist[3] }}</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}</p>
<p>A value from an object's method: {{ myobj.somemethod() }}</p>
```

##### Filters
- `{{ variable | filter }}` 구문을 사용하여 변수를 변환할 수 있다.
| Filter | Description |
| --- | --- |
| safe | HTML escaping을 하지 않음 |
| capitalize | 첫 글자를 대문자로 변환 |
| lower | 모든 문자를 소문자로 변환 |
| upper | 모든 문자를 대문자로 변환 |
| title | 각 단어의 첫 글자를 대문자로 변환 |
| trim | 문자열의 앞뒤 공백을 제거 |
| striptags | 랜더링 전 존재하는 HTML 태그를 제거 |

##### Control Structures
- Jinja2는 템플릿에서 `if`, `for` 등의 제어 구조를 사용할 수 있다.
```html
{% if user %}
    <h1>Hello, {{ user }}!</h1>
{% else %}
    <h1>Hello, Stranger!</h1>
{% endif %}

{% for comment in comments %}
    <li>{{ comment }}</li>
{% endfor %}
```

##### Macros
- `macro`는 템플릿에서 재사용 가능한 블록을 정의하는 데 사용할 수 있다.

##### Inherit
- `extends`와 `block`을 사용하여 템플릿을 상속할 수 있다.

### Flask-Bootstrap
- Flask-Bootstrap은 Flask와 Jinja2 템플릿 엔진을 사용하여 Bootstrap CSS 프레임워크를 사용할 수 있게 해준다.
```bash
$ pip install flask-bootstrap
```
```python
from flask_bootstrap import Bootstrap
...
bootstrap = Bootstrap(app)
```
## References
- [Flask의 세계에 오신것을 환영합니다. — Flask 0.11-dev documentation](https://flask-docs-kr.readthedocs.io/ko/latest/)
- [Quickstart — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
