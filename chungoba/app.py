# -*- coding:utf8 -*-
import sys
import linecache
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful_swagger_2 import Api
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # @app.errorhandler(Exception)
    # def global_exception_handler(err):
    #     exc_type, exc_obj, tb = sys.exc_info()
    #     f = tb.tb_frame
    #     lineno = tb.tb_lineno
    #     filename = f.f_code.co_filename
    #     linecache.checkcache(filename)
    #     line = linecache.getline(filename, lineno, f.f_globals)
    #     date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     str = '[{}] {}, LINE {} "{}": {}\n'.format(
    #         date, exc_obj, filename, lineno, line.strip())

    #     filepath = 'lebit/error_log/{}'.format(datetime.datetime.now().strftime('%Y-%m-%d'))
    #     f = open(filepath, 'a+')
    #     f.write(str)
    #     f.close()
    #     return 'Server Error : error_log 확인해주세요', 500

    app.config.from_object('chungoba.config.{0}'.format(config_name))

    db.init_app(app)

    api = Api(app, api_version='0.0', api_spec_url='/api/spec', title='chungoba spec', catch_all_404s=True)

    from .api.user import User
    
    # user
    api.add_resource(User, '/user')
    
    swaggerui_blueprint = get_swaggerui_blueprint('/api/docs', '/api/spec.json', config={'app_name': 'chungoba'})
    app.register_blueprint(swaggerui_blueprint, url_prefix='/api/docs')

    return app