from flask import Flask, send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/')
def game():
    with open("./build/web/index.html", "r") as s:
    	return s.read()


@app.route('/game.apk')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def apk():
    return send_file("./build/web/game.apk")


@app.route('/favicon.png')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def favicon():
    return send_file("./build/web/favicon.png")


if __name__ == '__main__':

    context = ('./ssl_keys/cert.pem', './ssl_keys/key.pem')
    cors = CORS(app, resources={r'*': {"origins": '*'}})
    
    app.run(debug=True, ssl_context=context, host="0.0.0.0")
