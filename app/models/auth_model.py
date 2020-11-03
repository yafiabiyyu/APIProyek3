from app import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)


class UserDoc(db.Document):
    username = db.StringField(required=True)
    password_hash = db.StringField(max_length=255, required=True)

    def GenerateHash(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(
            pwhash=self.password_hash, password=password
        )


class RevokedTokenDoc(db.Document):
    jti = db.StringField(max_length=120)

    def IsJtiBlackListed(jti):
        Query = RevokedTokenDoc.objects(jti=jti).first()
        return bool(Query)
