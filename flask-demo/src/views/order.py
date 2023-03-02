from flask import Blueprint, render_template, session, request, redirect
from utils import db
import random
from datetime import datetime

od = Blueprint("order", __name__)


@od.route("/order/list")
def order_list():
    # 获取用户信息
    user_id = session['userInfo']["id"]
    sql = "select * from task where user_id=%s order by user_id desc"
    data_list = db.fetch_all(sql, [user_id, ])
    return render_template("order_list.html", data_list=data_list)


@od.route("/order/add", methods=["GET", "POST"])
def order_add():
    if request.method == "GET":
        return render_template("order_add.html")
    # 获取数据
    url = request.form.get('url')
    count = request.form.get('count')

    order_id = "{}{}".format(datetime.now().strftime("%Y%m%d%H%M%S"), random.randint(1000, 9999))
    # 插入数据
    user_id = session.get("userInfo")["id"]
    sql = "insert into task(order_id, url ,count ,status, user_id)  values (%s,%s,%s,%s,%s )"
    db.commit(sql, [order_id, url, count, 1, user_id])
    # 跳转回登录页面
    return redirect("/order/list")


@od.route("/order/delete")
def order_delete():
    # http://127.0.0.1:5000/order/delete?nid=4
    # 获取参数
    nid = request.args.get('nid')
    # 执行sql语句
    sql = "delete from task where id=%s"
    db.commit(sql, [nid, ])
    # 跳转回list页面
    return redirect("/order/list")
