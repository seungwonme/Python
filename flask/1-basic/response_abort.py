from flask import Flask, abort

app = Flask(__name__)

def load_user(id):
    return None

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(400)
    return '<h1>Hello, %s</h1>' % user.name

if __name__ == '__main__':
    app.run()
