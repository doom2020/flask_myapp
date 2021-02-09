from flask import Blueprint, session
from flask import request
from flaskr import db
from ast import literal_eval
from ..models.model import UserInfo
import json

login = Blueprint('login_api', __name__)


@login.route('/login', methods=["GET"], endpoint='login_g')
def login_view_g():
    return 'login page'


@login.route('/login', methods=["POST"], endpoint='login_p')
def login_view_p():
    # request.data为u'' 转str
    # post_data = literal_eval(request.data.decode('utf8'))
    post_data = request.get_json(silent=True)
    user_name = post_data.get('user_name', None)
    # 通过hash解密
    password = post_data.get('password', None)
    print(f'request args ---> user_name: {user_name},password: {password}')
    if not user_name or not password:
        ret_dict = {
            "code": 400,
            "message": 'not user_name or not password',
            "result": []
        }
        return json.dumps(ret_dict)
    try:
        user_info_obj = UserInfo.query.filter(UserInfo.username == user_name, UserInfo.password == password,
                                              UserInfo.is_delete == 0).one()
    except Exception as e:
        ret_dict = {
            "code": 501,
            "message": 'query fail: %s' % e,
            "result": []
        }
        return json.dumps(ret_dict)
    if not user_info_obj:
        ret_dict = {
            "code": 502,
            "message": 'query result is None',
            "result": []
        }
        return json.dumps(ret_dict)
    # 生成session_id 存储

    ret_dict = {
        "code": 200,
        "message": 'success',
        "result": []
    }
    return json.dumps(ret_dict)
