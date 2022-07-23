from flask import Flask
from app import api

""" api (blueprints) """
from app.api.index import index
from app.api.error_handler import error_handler
from app.api.user import user
def create_flask_app(config):
    # application factory 생성
    app = Flask(
        import_name=__name__, # 패키지의 이름
        instance_relative_config=True,
        static_url_path='/', # 정적 폴더 기본 경로 설정
        static_folder='asset/static', # static 폴더 경로 설정
        template_folder='asset/templates'# templates 폴더 경로 설정
        ) 

    # config.py의 환경을 application에 적용한다.
    app.config.from_object(config)
    config.init_app(app)


    # api http request handling 설정
    api.init_app(app)

    # db connection pool
    # register_connection_pool(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(error_handler.bp)
    app.register_blueprint(user.bp)
    return app
