from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def myfunc(data):
    emit('my response', data)

    #print(data)


if __name__ == '__main__':
    socketio.run(app)