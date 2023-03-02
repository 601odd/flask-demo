from flask import Flask, session, redirect, request

from .views import account
from .views import order


# 注册全局函数
def get_user_phone():
    return session['userInfo']['phone']


# 每个请求前执行的钩子函数 验证
def auth():
    if request.path.endswith('/'):
        return redirect("/login")
    if request.path.startswith('/login'):
        return
    if request.path.startswith('/static'):
        return
    name = session.get('userInfo')
    if not name:
        return redirect("/login")


def create_app():
    app = Flask(__name__)
    app.template_global()(get_user_phone)
    app.before_request(auth)

    # 注册蓝图
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)

    return app
