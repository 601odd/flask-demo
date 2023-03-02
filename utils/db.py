import pymysql
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB

# 创建连接池: 20连接
POOL = PooledDB(
    creator=pymysql,
    maxconnections=20,
    mincached=2,
    blocking=True,
    host="127.0.0.1", port=3306, user="root", passwd="159357oxy..", charset="utf8", db='ordersTable'
)

def fetch_one(sql, params):
    # 连接MySQL，去连接池中获取一个连接
    conn = POOL.connection()
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute(sql, params)
    row_dict = cursor.fetchone()
    # 归还到连接池
    cursor.close()
    conn.close()
    return row_dict


def fetch_all(sql, params):
    # 连接MySQL，去连接池中获取一个连接
    conn = POOL.connection()
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute(sql, params)
    data_list = cursor.fetchall()
    # 归还到连接池
    cursor.close()
    conn.close()
    return data_list


def commit(sql, params):
    # 连接MySQL，去连接池中获取一个连接
    conn = POOL.connection()
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute(sql, params)
    conn.commit()
    # 归还到连接池
    cursor.close()
    conn.close()
