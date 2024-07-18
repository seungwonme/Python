from flask import Flask, current_app, g

app = Flask(__name__)

# 애플리케이션 컨텍스트를 명시적으로 생성
with app.app_context():
    # current_app 객체를 사용하여 현재 애플리케이션의 이름을 출력
    print(current_app.name)

    # g 객체를 사용하여 일부 데이터를 저장하고 출력
    g.some_data = 'This is some example data'
    print(g.some_data)

# 이 시점에서는 애플리케이션 컨텍스트가 종료되었으므로 current_app과 g에 접근할 수 없습니다.
  
# print(current_app.name) # AttributeError: 'NoneType' object has no attribute 'name'
# print(g.some_data) # RuntimeError: Working outside of application context.
