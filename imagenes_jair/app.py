from flask import Flask

app = Flask(__name__)

@app.route('/')
def ejemplo():
    return 'Hola mundo, esta es una API de Flask dockerizada'

if __name__=='__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)