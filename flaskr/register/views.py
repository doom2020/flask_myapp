from flask import Blueprint
from flask import request
import json
from ..models.model import UserInfo
from sqlalchemy import or_
import hashlib
import base64
from datetime import datetime
from flaskr import db

register = Blueprint('register_api', __name__)


@register.before_request
def before_request_handler():
    pass


@register.route('/register', methods=['GET'], endpoint='register_g')
def register_view_g():
    return 'register page'


@register.route('/register', methods=['POST'], endpoint='register_p')
def register_view_p():
    post_data = request.get_json(silent=True)
    # print(post_data)
    user_name = post_data.get('user_name', None)
    phone = post_data.get('phone', None)
    pwd = post_data.get('pwd', None)
    upwd = post_data.get('upwd', None)
    print(f'request args --> user_name:{user_name}, phone:{phone}, pwd:{pwd}, upwd:{upwd}')
    # 信息不全
    if not user_name or not phone or not pwd or not upwd:
        ret_dict = {
            "code": 400,
            "message": 'not user_name or not phone or not pwd or not upwd',
            "result": []
        }
        return json.dumps(ret_dict)
    # 密码确认异常
    if pwd != upwd:
        ret_dict = {
            "code": 401,
            "message": 'pwd is different upwd',
            "result": []
        }
        return json.dumps(ret_dict)
    # 通过base64加密手机号存储
    encrypt_phone = base64.b64encode(phone.encode('utf8'))
    print(f'加密的号码: {encrypt_phone}')
    # 查询出错
    try:
        user_info_obj = UserInfo.query.filter(or_(UserInfo.username == user_name, UserInfo.phone == encrypt_phone)).all()
    except Exception as e:
        ret_dict = {
            "code": 501,
            "message": 'query fail: %s' % e,
            "result": []
        }
        return json.dumps(ret_dict)
    # 查询结果已存在
    if user_info_obj:
        ret_dict = {
            "code": 502,
            "message": 'username or phone has existed',
            "result": []
        }
        return json.dumps(ret_dict)
    # 通过hash加密密码存储
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    encrypt_pwd = md5.hexdigest()
    print(f'加密的密码: {encrypt_pwd}')
    c_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    u_time = c_time
    # 存储数据到mysql(异常则回滚)
    try:
        new_user = UserInfo(username=user_name, phone=encrypt_phone, password=encrypt_pwd, c_time=c_time, u_time=u_time,
                            is_delete=0)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.close()
        ret_dict = {
            "code": 503,
            "message": 'register fail: %s' % e,
            "result": []
        }
        return json.dumps(ret_dict)
    ret_dict = {
        "code": 200,
        "message": 'success',
        "result": []
    }
    print("注册成功")
    return json.dumps(ret_dict)


@register.after_request
def after_request_handler(response):
    return response
