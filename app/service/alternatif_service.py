from ..models.alternatif_model import AlternatifDoc


class AlternatifService:
    def add_alternatif(self, data):
        check_alternatif = AlternatifDoc.objects(
            _id=data["_id"]
        ).first()
        if check_alternatif is not None:
            message_object = {
                "status": "gagal",
                "message": "Data alternatif telah terdaftar",
            }
            return message_object
        else:
            try:
                save_alternatif = AlternatifDoc(
                    _id=data["_id"],
                    nama_mahasiswa=data["nama_mahasiswa"],
                    alamat=data["alamat"],
                    jenis_kelamin=data["jenis_kelamin"],
                    subkriteria_id=data["subkriteria_id"],
                ).save()
                message_object = {
                    "status": "berhasil",
                    "message": "Data alternatif telah tersimpan",
                }
                return message_object
            except Exception as e:
                message_object = {"status": "gagal", "message": e}
                return message_object

    def get_all_data(self):
        try:
            data = list(AlternatifDoc.objects().all())
            print(data)
            return data
        except Exception as e:
            message_object = {"status": "gagal", "message": e}
            return message_object

    def get_alternatif_by_nim(self, nim):
        data = AlternatifDoc.objects(_id=nim).first()
        if data is None:
            message_object = {
                "status": "gagal",
                "message": "Alternatif dengan nim {} tidak ditemukan".format(
                    nim
                ),
            }
            return message_object
        else:
            return data

    def update_alternatif(self, nim, data):
        check_alternatif_data = AlternatifDoc.objects(_id=nim).first()
        if check_alternatif_data is not None:
            try:
                check_alternatif_data._id = data["_id"]
                check_alternatif_data.nama_mahasiswa = data[
                    "nama_mahasiswa"
                ]
                check_alternatif_data.alamat = data["alamat"]
                check_alternatif_data.jenis_kelamin = data[
                    "jenis_kelamin"
                ]
                check_alternatif_data.subkriteria_id = data[
                    "subkriteria_id"
                ]
                check_alternatif_data.save()
                message_object = {
                    "status": "berhasil",
                    "message": "Data alternatif telah diperbarui",
                }
                return True, message_object
            except Exception as e:
                message_object = {"status": "gagal", "message": e}
                return False, message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Kriteria {} tidak ditemukan".format(
                    data[nama_subkriteria]
                ),
            }
            return False, message_object

    def delete_alternatif(self, nim):
        delete_alternatif_nim = AlternatifDoc.objects(_id=nim).first()
        if delete_alternatif_nim is not None:
            delete_alternatif_nim.delete()
            message_object = {
                "status": "berhasil",
                "message": "Alternatif dengan Nim {} berhasil di hapus".format(
                    nim
                ),
            }
            return message_object
        else:
            message_object = {
                "status": "gagal",
                "message": "Alternatif dengan nim {} tidak ditemukan".format(
                    nim
                ),
            }
            return message_object
