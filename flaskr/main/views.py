from flask import Blueprint, session, redirect
from ..models.model import UserInfo
index = Blueprint('index_api', __name__)


@index.route('/', methods=['GET'])
def index_view():
    user_info = session.get('uname')
    user = UserInfo.query.filter(UserInfo.username == 'yuan').all()
    print(user)
    if user_info:
        print(user_info)
        return 'index page'
    else:
        return redirect('/api/login')
