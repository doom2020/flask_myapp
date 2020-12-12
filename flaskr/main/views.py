from flask import Blueprint, session, request, redirect

index = Blueprint('index_api', __name__)


@index.route('/', methods=['GET'])
def index_view():
    user_info = session.get('uname')
    if user_info:
        print(user_info)
        return 'index page'
    else:
        return redirect('/api/login')