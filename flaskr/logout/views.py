from flask import Blueprint, session

logout = Blueprint('logout_api', __name__)

@logout.route('/logout', methods=['GET'], endpoint='logout')
def logout_view():
    del session['uname']
    return 'logout page'