from flask import Flask,render_template,url_for,redirect
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde Railway en Python!'

@app.route('/home')
def home():
    dato = 'Mi Dato'
    return render_template('index.html', dato = dato)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))