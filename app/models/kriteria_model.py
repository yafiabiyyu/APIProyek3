from app import db


class KriteriaDoc(db.Document):
    _id = db.StringField(required=True, max_length=15)
    nama_kriteria = db.StringField(required=True, max_length=50)
    atribut = db.StringField(required=True, max_length=10)
    bobot = db.FloatField(required=True)
