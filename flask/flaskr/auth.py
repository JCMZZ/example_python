import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# 生成蓝图实例对象 参数: 名称，定义位置，再所有与蓝图有关的URL前添加子段url_prefix('/auth/register')
bp = Blueprint('auth', __name__, url_prefix='/auth')
# 注册视图路由 包括'GET'和'POST'方法
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # POST请求执行
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    # GET请求执行
    return render_template('auth/register.html')