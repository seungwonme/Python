from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_comments():
    comments = [
        "Flask는 정말 멋진 마이크로 웹 프레임워크입니다.",
        "Jinja2 템플릿은 사용하기 편리합니다.",
        "매크로 기능은 코드 재사용성을 높여줍니다."
    ]
    return render_template('macro.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
