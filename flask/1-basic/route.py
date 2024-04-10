from flask import Flask # Flask 웹 프레임워크에서 Flask 클래스를 import
app = Flask(__name__) # Flask 클래스의 인스턴스 생성

@app.route('/') # 루트 URL에 대한 라우트
def index(): # URL을 처리하는 함수(view function)
    return '<h1>Hello, World!</h1>' # 클라이언트에게 반환할 Response

@app.route('/user/<name>') # /user/<name> URL에 대한 라우트
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# http://127.0.0.1:5000/userid/[id]로 접속하면 id에 해당하는 숫자가 출력
# 정수가 아닌 문자열을 입력하면 404 Not Found 에러 발생
@app.route('/userid/<int:id>') # /user/<id> URL에 대한 라우트, id는 정수형으로 변환
def userid(id):
    return '<h1>Hello, Your ID is %d!</h1>' % id

if __name__ == '__main__': # 현재 스크립트 파일이 프로그램으로 실행될 때만 실행
    app.run() # 내장 웹 서버 실행
