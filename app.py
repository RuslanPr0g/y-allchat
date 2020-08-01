from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fk;'  # it needs to get rid of that in the future
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    print('14:02 - ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
