from flask_swagger.swagger import Swagger
import logging

import jsonschema
from flask import Flask, jsonify
from flask import make_response
from .config import Config

url_prefix="/api/v1"
swagger = Swagger()

def init_router(app):
    from .api import api
    from .main import main
    from flask_cors import CORS
    CORS(app, supports_credentials=True)
    app.register_blueprint(api, url_prefix=url_prefix)
    app.register_blueprint(main)

def create_app():
    app = Flask(__name__)
    app.config.update(Config or {})
    logging.basicConfig(level=logging.DEBUG)


    @app.errorhandler(jsonschema.ValidationError)
    def handle_bad_request(e):
        return make_response(jsonify(code=400,
             message=e.schema.get('error', '参数校验错误'),
             details=e.message,
             schema=str(e.schema)), 200)

    @app.before_request
    def setup_context():
        from flask import request
        r = request.view_args
        pass

    swagger.init_app(app)
    init_router(app)
    return app