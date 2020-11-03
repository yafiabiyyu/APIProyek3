from app.models.auth_model import UserDoc, RevokedTokenDoc
from flask_jwt_extended import create_access_token, create_refresh_token


def LoginService(data):
    get_auth_data = UserDoc.objects(username=data["username"]).first()
    if get_auth_data is None:
        message_object = {
            "status": "gagal",
            "message": "Username {} tidak ditemukan".format(
                data["username"]
            ),
        }
        return message_object
    elif get_auth_data is not None and get_auth_data.verify_password(
        data["password"]
    ):
        JwtAccessToken = create_access_token(identity=data["username"])
        RefreshToken = create_refresh_token(identity=data["username"])
        message_object = {
            "status": "berhasil",
            "message": "Pengguna {} berhasil login".format(
                data["username"]
            ),
            "access_token": JwtAccessToken,
            "refresh_token": RefreshToken,
        }
        return message_object
    else:
        return {
            "status": "gagal",
            "message": "Kesalahan username atau password",
        }


def LogoutService(jti):
    revoked_token = RevokedTokenDoc(jti=jti).save()
    if revoked_token:
        message_object = {
            "status": "berhasil",
            "message": "Berhasil logout",
        }
        return message_object
    else:
        message_object = {"status": "gagal", "message": "Gagal logout"}
