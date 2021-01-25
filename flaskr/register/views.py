from flask import Blueprint

register = Blueprint('register_api', __name__)

@register.before_request
def before_request_handler():
    pass

@register.route('/register', methods=['GET'], endpoint='register_g')
def register_view_g():
    return 'register page'

@register.route('/register', methods=['POST'], endpoint='register_p')
def register_view_p():
    return 'register post'

@register.after_request
def after_request_handler(response):
    return response