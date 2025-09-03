from db.user import User
from db.session import Session
import view.message as msg
from utils.common import *


def get_user_info(form):

    if not assert_keys_in_form_exist(form, ['sessionID']):
        return msg.error_msg("Invalid request.")

    session_id = form['sessionID']
    session = Session.get_session(session_id)
    if len(session) == 0:
        return msg.error_msg("Unable to find the session.")

    (sessionid, uid, start_time, end_time) = session[0].values()
    user = User.get_user(uid=uid)

    if len(user) == 0:
        return msg.error_msg("Unable to find the user")

    (uid, name, email, phone, password, enable) = user[0].values()

    return msg.success_msg({"uid": uid, "name": name, "email": email, "phone": phone})


def update_user(form):

    if not assert_keys_in_form_exist(form, ['sessionID', 'name', 'email', 'phone', 'newPassword']):
        return msg.error_msg("Invalid request.")

    name = form['name']
    session_id = form['sessionID']
    email = form['email']
    phone = form['phone']
    new_password = form['newPassword']

    if new_password.strip() == "":
        return msg.error_msg("Password cannot be empty.")

    if len(name) > 255:
        return msg.error_msg("Username cannot exceed 255 characters.")

    if len(new_password) > 255:
        return msg.error_msg("Password cannot exceed 255 characters.")

    # Get User according to sessionID
    session = Session.get_session(session_id)
    if len(session) == 0:
        return msg.error_msg("Unable to find the session.")

    (sessionid, uid, start_time, end_time) = session[0].values()

    args = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Password": encrypt(new_password),
        "UID": uid
    }
    ret = User.update_user(args)

    if ret is None:
        return msg.error_msg("Failed to update user profile.")

    return msg.success_msg({})


def delete_user(form):

    if not assert_keys_in_form_exist(form, ['sessionID', 'password']):
        return msg.error_msg("Invalid request.")

    password = form['password']
    session_id = form['sessionID']

    # Get User according to sessionID
    session = Session.get_session(session_id)

    if len(session) == 0:
        return msg.error_msg("Unable to find the session.")

    (sessionid, uid, start_time, end_time) = session[0].values()

    if end_time is not None:
        return msg.error_msg("Expired SessionID")

    # Verify password
    if password.strip() == "":
        return msg.error_msg("Password cannot be empty.")

    findUser = User.get_user(uid=uid, password=encrypt(password), enable=True)
    if findUser is None:
        return msg.error_msg("Failed to find user.")

    if len(findUser) == 0:
        return msg.error_msg("Wrong password.")

    # Delete User
    ret = User.delete_user(uid)

    if ret is None:
        return msg.error_msg("Failed to delete user.")

    # Revoke all sessions
    Session.end_session(uid=uid)

    return msg.success_msg({"uid": uid, "sessionID": session_id})


def add_user(form):

    if not assert_keys_in_form_exist(form, ['name', 'email', 'phone', 'password']):
        return msg.error_msg("Invalid request.")

    name = form['name']
    email = form['email']
    phone = form['phone']
    password = form['password']

    if password.strip() == "":
        return msg.error_msg("Password cannot be empty.")

    if len(name) > 255:
        return msg.error_msg("Username cannot exceed 255 characters.")

    if len(password) > 255:
        return msg.error_msg("Password cannot exceed 255 characters.")

    findUser = User.get_user(email=email, enable=True)
    if findUser is None:
        return msg.error_msg("Failed to find user.")

    if len(findUser) != 0:
        return msg.error_msg("User already exists.")

    args = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Password": encrypt(password),
        "Enable": True
    }
    res = User.add_user(args)
    if res is None:
        return msg.error_msg("Failed to add user.")

    return msg.success_msg({"msg": "User added successfully."})
