from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Connect to 10.23.5.34:9999 when a client connects
    emit('connect_to_server', {'server_address': '10.23.5.34:9999'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    # Broadcast the message to all connected clients
    socketio.emit('message', message)

if __name__ == '__main__':
    # Run the app on IP address 10.23.5.34 and port 9999
    socketio.run(app, host='10.23.5.34', port=9999)
