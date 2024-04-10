from flask import Flask, request

app = Flask(__name__)

# @app.before_first_request
# def before_first_request():
#     print("첫 번째 요청이 처리되기 전에 실행됩니다.")

@app.before_request
def before_request():
    print("매 요청이 처리되기 전에 실행됩니다.")

@app.after_request
def after_request(response):
    print("매 요청이 처리된 후에 실행됩니다.")
    response.headers["Content-Type"] = "application/json"
    return response

@app.teardown_request
def teardown_request(exception=None):
    print("매 요청이 처리된 후에 실행됩니다. 예외가 발생해도 실행됩니다.")

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
