# -*- conding:UTF-8 -*-
import os
from flask import Flask

#创建一个应用并配置
def create_app(test_config=None):
    #实例对象配置
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # 加载实例配置，如果它存在，则不进行测试
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 如果存在，请载入测试配置
        app.config.from_mapping(test_config)

    # 确保实例文件夹的存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 一个简单的页面，上面写着hello
    @app.route('/hello')
    def hello():
        return '<h1 style="color:red;">Hello, World!</h1>'
    
    # 注册数据库 init
    from . import db
    db.init_app(app)
    # 注册蓝图
    from . import auth
    app.register_blueprint(auth.bp)

    return app
