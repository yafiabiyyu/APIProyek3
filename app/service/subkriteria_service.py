from ..models.kriteria_model import SubkriteriaDoc, KriteriaDoc
from uuid import uuid4


class SubkriteriaService:
    def add_subkriteria(self, data):
        get_kriteria_doc = KriteriaDoc.objects(
            _id=data["kode_kriteria"]
        ).first()
        get_kriteria_doc.save()
        check_subkriteria = SubkriteriaDoc.objects(
            nama_subkriteria=data["nama_subkriteria"]
        ).first()
        if check_subkriteria is None:
            try:
                save_data_subkriteria = SubkriteriaDoc(
                    _id=str(uuid4())[:8],
                    jenis_kriteria=get_kriteria_doc.to_dbref(),
                    nama_subkriteria=data["nama_subkriteria"],
                    nilai=data["nilai"],
                ).save()
                message_object = {
                    "status": "berhasil",
                    "message": "Data subkriteria {} berhasil ditambahkan".format(
                        data["nama_subkriteria"]
                    ),
                }
                return message_object
            except Exception as e:
                message_object = {"status": "gagal", "message": e}
                return message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Subkriteria {} telah terdaftar".format(
                    data["nama_subkriteria"]
                ),
            }
            return message_object

    def update_subkriteria(self, kode_subkriteria, data):
        check_subkriteria_data = SubkriteriaDoc.objects(
            _id=kode_subkriteria
        ).first()
        get_kriteria_id = KriteriaDoc.objects(
            _id=data["jenis_kriteria"]
        ).first()
        if check_subkriteria_data is not None:
            try:
                check_subkriteria_data._id = data["_id"]
                check_subkriteria_data.jenis_kriteria = get_kriteria_id
                check_subkriteria_data.nama_subkriteria = data[
                    "nama_subkriteria"
                ]
                check_subkriteria_data.nilai = data["nilai"]
                check_subkriteria_data.save()
                message_object = {
                    "status": "berhasil",
                    "message": " Subkriteria {} berhasil diperbarui".format(
                        data["nama_subkriteria"]
                    ),
                }
                return True, message_object
            except Exception as e:
                message_object = {"status": "gagal", "message": e}
                return True, message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Kriteria {} tidak ditemukan".format(
                    data[nama_subkriteria]
                ),
            }
            return False, message_object

    def delete_subkriteria(self, kode_subkriteria):
        delete_subkriteria_by_id = SubkriteriaDoc.objects(
            _id=kode_subkriteria
        ).first()
        if delete_subkriteria_by_id is not None:
            delete_subkriteria_by_id.delete()
            message_object = {
                "status": "berhasil",
                "message": "Subkriteria dengan ID {} berhasil di hapus".format(
                    kode_subkriteria
                ),
            }
            return message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Subkriteria dengan ID {} tidak ditemukan".format(
                    kode_subkriteria
                ),
            }
            return message_object

    def get_list_subkriteria_data(self, kode_kriteria):
        return list(
            SubkriteriaDoc.objects(jenis_kriteria=kode_kriteria).all()
        )

    def get_subkriteria_data(self, kode_subkriteria):
        return list(
            SubkriteriaDoc.objects(
                jenis_kriteria=kode_subkriteria
            ).all()
        )
