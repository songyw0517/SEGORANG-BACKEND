'''
Application Config Setting
'''
import os

# 기본 설정
APP_NAME = "SEGORANG_FLASK"
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Config 클래스
class Config:
    '''General Config'''
    SLOW_API_TIME = 0.5
    JSON_AS_ASCII = False
    SECRET_KEY = "top-secret"

    @staticmethod
    def init_app(app):
        pass

# TestConfig 클래스
class TestConfig(Config):
    DEBUG = True
    TESTING = True

config=TestConfig