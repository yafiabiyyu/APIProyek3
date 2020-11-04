from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS
import datetime
import os

load_dotenv()
db = MongoEngine()
jwt = JWTManager()
cors = CORS()


def create_app(config_name):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        JWT_SECRET_KEY=os.getenv("JWT_KEY"),
        JWT_BLACKLIST_ENABLED=True,
        JWT_BLACKLIST_TOKEN_CHECKS=["access", "refresh"],
    )
    # Where to look for the JWT. Available options are cookies or headers
    app.config.setdefault("JWT_TOKEN_LOCATION", ("headers",))
    # Options for JWTs when the TOKEN_LOCATION is headers
    app.config.setdefault("JWT_HEADER_NAME", "Authorization")
    app.config.setdefault("JWT_HEADER_TYPE", "Bearer")
    app.config["MONGODB_SETTINGS"] = {"host": os.getenv("mongodb_uri")}
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from app.models import auth_model, kriteria_model

    @jwt.token_in_blacklist_loader
    def CheckIfTokenInBlacklist(decrypted_token):
        jti = decrypted_token["jti"]
        return auth_model.RevokedTokenDoc.IsJtiBlackListed(jti)
        # return user_model.RevokedTokenModel.IsJtiBlackListed(jti)

    from .controller import controller as CtrlBlueprint

    app.register_blueprint(CtrlBlueprint, url_prefix="/api/v1")
    app.app_context().push()

    return app
