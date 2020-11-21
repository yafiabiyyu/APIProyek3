from ..models.kriteria_model import KriteriaDoc
from app import db
from uuid import uuid4


class KriteriaService:
    def add_kriteria(self, data):
        get_kriteria = KriteriaDoc.objects(
            nama_kriteria=data["nama_kriteria"]
        ).first()
        if get_kriteria is None:
            try:
                save_kriteria = KriteriaDoc(
                    _id=str(uuid4())[:8],
                    nama_kriteria=data["nama_kriteria"],
                    atribut=data["atribut"],
                    bobot=float(data["bobot"]),
                ).save()
                message_object = {
                    "status": "berhasil",
                    "message": "Data Kriteria {} berhasil ditambahkan".format(
                        data["nama_kriteria"]
                    ),
                }
                return message_object
            except Exception as e:
                message_object = {"status": "gagal", "message": e}
                return message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Kriteria {} telah terdaftar".format(
                    data["nama_kriteria"]
                ),
            }
            return message_object

    def update_kriteria(self, kode, data):
        check_kriteria_data = KriteriaDoc.objects(_id=kode).first()
        if check_kriteria_data is not None:
            try:
                check_kriteria_data._id = data["_id"]
                check_kriteria_data.nama_kriteria = data[
                    "nama_kriteria"
                ]
                check_kriteria_data.atribut = data["atribut"]
                check_kriteria_data.bobot = data["bobot"]
                check_kriteria_data.save()
                message_object = {
                    "status": "berhasil",
                    "message": "Kriteria {} berhasil diperbarui".format(
                        data["nama_kriteria"]
                    ),
                }
                return True, message_object
            except Exception as e:
                message_object = {
                    "status": "gagal",
                    "message": "{}".format(e),
                }
                return False, message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Kriteria {} tidak ditemukan".format(
                    data[nama_kriteria]
                ),
            }
            return False, message_object

    def get_spesifik_kriteria(self, _id):
        data = KriteriaDoc.objects(_id=_id).first()
        if data is None:
            message_object = {
                "status": "gagal",
                "message": "Kriteria dengan ID {} tidak ditemukan".format(
                    _id
                ),
            }
            return message_object
        else:
            return data

    def get_all_data(self):
        try:
            data = list(KriteriaDoc.objects().all())
            print(data)
            return data
        except Exception as e:
            message_object = {"status": "gagal", "message": e}
            return message_object

    def ambil_bobot(self):
        id_kriteria = []
        nama_kriteria = []
        bobot_list = []
        perbaikan_bobot = []
        data_bobot = []
        data_kriteria = KriteriaDoc.objects().all()
        for data in range(0, len(data_kriteria)):
            id_kriteria.append(data_kriteria[data]._id)
            nama_kriteria.append(data_kriteria[data].nama_kriteria)
            bobot_list.append(data_kriteria[data].bobot)
        total_bobot = sum(bobot_list)
        for i in range(0, len(bobot_list)):
            perbaikan_bobot.append(bobot_list[i] / total_bobot)
        for data in range(0, len(id_kriteria)):
            dict_bobot = {
                "_id": id_kriteria[data],
                "nama_kriteria": nama_kriteria[data],
                "bobot": perbaikan_bobot[data],
            }
            data_bobot.append(dict_bobot)
        return data_bobot
