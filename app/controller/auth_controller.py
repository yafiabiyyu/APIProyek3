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
from ..service.auth_service import LoginService, LogoutService

api = Namespace("Auth", "Endpoint Untuk Authentications")
auth_data = api.model(
    "login",
    {
        "username": fields.String(
            required=True,
            description="Username dari user yang telah terdaftar",
        ),
        "password": fields.String(
            required=True,
            description="Password dari user yang telah terdaftar",
        ),
    },
)


@api.route("/login")
class LoginResource(Resource):
    @api.doc(
        responses={200: "OK", 400: "Bad Request"},
        description="Endpoint untuk login",
    )
    @api.expect(auth_data)
    def post(self):
        try:
            GetUserData = request.json
            print(GetUserData["username"])
            LoginStatus = LoginService(GetUserData)
            return jsonify(LoginStatus)
        except Exception as e:
            api.abort(400, e)


@api.route("/logout")
class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        try:
            RevokedToken = LogoutService(jti)
            return jsonify(RevokedToken)
        except Exception:
            return jsonify(
                {"status": "gagal", "message": "terjadi kesalahan"}
            )
