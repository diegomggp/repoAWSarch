from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mensaje = "¡Bienvenidos a mi aplicación web!"
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
# comment
