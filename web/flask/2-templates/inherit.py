from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 타이틀 변수를 설정합니다. 이 변수는 extends.html에 전달되어 사용됩니다.
    return render_template('extends.html', title='Home Page')

if __name__ == '__main__':
    app.run(debug=True)
