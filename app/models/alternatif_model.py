from app import db

class AlternatifDoc(db.Document):
    _id = db.StringField(required=True, primary_key=True, max_length=15)
    nama_mahasiswa = db.StringField(required=True,max_length=50)
    alamat = db.StringField(required=True,max_length=50)
    jenis_kelamin = db.StringField(required=True,max_length=15)
    subkriteria_id = db.ListField(db.StringField())
    
