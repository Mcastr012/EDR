#!/usr/bin/python3
from flask import Flask
from flask import request
from config import *
import controller.behavior as behavior_controller
import controller.user as user_controller
import controller.session as session_controller
import view.message as msg

app = Flask(__name__)


@app.route('/api/behavior', methods=['POST'])
def update_data():
    return behavior_controller.load_behavior(request.json)


@app.route("/api/behavior", methods=['GET'])
def get_behavior():
    behavior = behavior_controller.get_behavior(request.json)
    return msg.success_msg(behavior)


@app.route("/api/abnormal", methods=['GET'])
def get_abnormal():
    abnormal = behavior_controller.get_abnormal(request.json)
    return msg.success_msg(abnormal)


# API - User System
@app.route('/api/user', methods=['GET'])
def get_user_info():
    return user_controller.get_user_info(request.json)


@app.route('/api/user', methods=['POST'])
def add_user():
    return user_controller.add_user(request.json)


@app.route('/api/user', methods=['DELETE'])
def delete_user():
    return user_controller.delete_user(request.json)


@app.route('/api/user', methods=['PUT'])
def update_user_info():
    return user_controller.update_user(request.json)


@app.route('/api/session', methods=['POST'])
def log_in():
    return session_controller.add_session(request.json)


@app.route('/api/session', methods=['DELETE'])
def log_out():
    return session_controller.delete_session(request.json)


if __name__ == '__main__':
    app.run(debug=APP_DEBUG_MODE, host=APP_HOST)
