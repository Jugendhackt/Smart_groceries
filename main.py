from flask import request, Flask
app = Flask(__name__)

@app.route('/login')
def login():
    error = None
    return request.args.get('name')

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port='8000', debug=True)


