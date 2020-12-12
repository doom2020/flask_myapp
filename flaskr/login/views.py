from flask import Blueprint, session

login = Blueprint('login_api', __name__)

@login.route('/login', methods=["GET"], endpoint='login_g')
def login_view_g():
    session['uname'] = 'yuan'
    return 'login page'

@login.route('/login', methods=["POST"], endpoint='login_p')
def login_view_p():
    return 'login post'