from app import create_flask_app
from config import config
application = create_flask_app(config)

if __name__ == '__main__':
    application.run()