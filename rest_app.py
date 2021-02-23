from flask import Flask, request
import db_connector
import os
import signal

app = Flask(__name__)


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):

    if request.method == 'GET':
        return db_connector.get_requests(user_id)

    elif request.method == 'POST':
        return db_connector.post_requests(user_id)

    elif request.method == 'PUT':
        return db_connector.put_requests(user_id)

    elif request.method == 'DELETE':
        return db_connector.delete_requests(user_id)


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
