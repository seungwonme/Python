from flask import Flask, make_response

app = Flask(__name__)

# 튜플 형태의 응답
# (응답, 상태코드(기본값 200), 헤더)
@app.route('/tuple')
def tuple_response():
    return '<h1>Hello, World!</h1>', 201, {'Content-Type': 'text/html'}

# Response 객체를 반환
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(debug=True)
