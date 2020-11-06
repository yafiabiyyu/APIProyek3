from app import db


class KriteriaDoc(db.Document):
    _id = db.StringField(required=True, primary_key=True, max_length=15)
    nama_kriteria = db.StringField(required=True, max_length=50)
    atribut = db.StringField(required=True, max_length=10)
    bobot = db.FloatField(required=True)


class SubkriteriaDoc(db.Document):
    _id = _id = db.StringField(
        required=True, primary_key=True, max_length=15
    )
    jenis_kriteria = db.ReferenceField("KriteriaDoc")
    nama_subkriteria = db.StringField(required=True, max_length=50)
    nilai = db.FloatField(required=True)
