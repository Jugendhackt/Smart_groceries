from flask import request, Flask

app = Flask(__name__)


@app.route('/login')
def hello_world2():
    error = None
    name = request.args.get('name')
    return "hallo"+name


@app.route('/')
def hello_world():
    return "hallo"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)

