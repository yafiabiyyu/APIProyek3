from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from werkzeug.exceptions import NotFound
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)

api = Namespace("Auth", "Endpoint Untuk Authentications")