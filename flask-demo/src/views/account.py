from flask import Blueprint, render_template, redirect, request, session
from utils import db

ac = Blueprint("account", __name__)


@ac.route("/login", methods=["POST", "GET"])
def login():
    # 获取用户信息
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        password = request.form.get('pwd')
        phone = request.form.get("phone")
    # 连接mysql
    raw_dict = db.fetch_one("select id, phone from userInfo where password=%s and phone=%s", [password, phone])
    if not raw_dict:
        return render_template("login.html", error="用户或者密码输入错误")
    # 登录成功
    session['userInfo'] = raw_dict
    # 跳转
    return redirect("/order/list")


@ac.route("/logout")
def logout():
    # 删除当前的会话信息
    session.clear()
    return redirect("/order/list")


@ac.route("/not-found")
def not_found():
    return "404 not-found"
